import httpx
from fastapi import APIRouter, Query
import math

router = APIRouter(prefix="/api/vets", tags=["Veterinary"])

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = math.sin(d_lat/2) * math.sin(d_lat/2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(d_lon/2) * math.sin(d_lon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

@router.get("/nearby")
async def get_nearby_vets(
    lat: float = Query(..., description="User latitude"),
    lng: float = Query(..., description="User longitude"),
    radius: int = Query(None, description="Search radius in meters"),
):
    """
    Find nearby veterinary hospitals using Overpass API (OpenStreetMap).
    Tries 5 km, 10 km, and 25 km sequentially if radius is not provided.
    """
    # Progressive search radii: 5km, 10km, 25km
    radii = [5000, 10000, 25000] if radius is None else [radius]
    overpass_url = "https://overpass-api.de/api/interpreter?utm_source=chatgpt.com"
    elements = []
    
    for r in radii:
        overpass_query = f"""
        [out:json][timeout:25];
        (
          node["amenity"="veterinary"](around:{r},{lat},{lng});
          way["amenity"="veterinary"](around:{r},{lat},{lng});
          relation["amenity"="veterinary"](around:{r},{lat},{lng});
        );
        out center;
        """
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(overpass_url, data={'data': overpass_query}, timeout=15.0)
                if resp.status_code == 200:
                    data = resp.json()
                    elements = data.get("elements", [])
                    if elements:
                        break  # Stop as soon as we find veterinary facilities
        except Exception as e:
            print(f"[WARN] Overpass query failed for radius {r}: {e}")

    try:
        if not elements:
            # Fallback demo data
            return {
                "results": [
                    {
                        "name": "Sri Veterinary Hospital (Demo)",
                        "address": "Main Road, Near Bus Stand",
                        "lat": lat + 0.008,
                        "lng": lng + 0.005,
                        "distance": f"{calculate_distance(lat, lng, lat + 0.008, lng + 0.005):.1f} km",
                        "phone": "+91 98765 43210",
                        "open_now": True,
                        "rating": 4.5,
                    },
                    {
                        "name": "Pashupathi Animal Clinic (Demo)",
                        "address": "Market Circle, 2nd Cross",
                        "lat": lat - 0.005,
                        "lng": lng + 0.012,
                        "distance": f"{calculate_distance(lat, lng, lat - 0.005, lng + 0.012):.1f} km",
                        "phone": "+91 98765 12345",
                        "open_now": True,
                        "rating": 4.2,
                    }
                ],
                "using_sample_data": True,
                "error": "No veterinary clinics found in your area on OpenStreetMap. Showing sample data."
            }

        results = []
        for el in elements:
            el_lat = el.get("lat") or el.get("center", {}).get("lat", 0)
            el_lng = el.get("lon") or el.get("center", {}).get("lon", 0)
            tags = el.get("tags", {})
            
            name = tags.get("name", tags.get("name:en", "Veterinary Clinic"))
            address = tags.get("addr:full", tags.get("addr:street", tags.get("addr:city", "Local Veterinary Service")))
            phone = tags.get("phone", tags.get("contact:phone", tags.get("mobile", "")))
            opening_hours = tags.get("opening_hours", "")
            
            dist_km = calculate_distance(lat, lng, el_lat, el_lng)
            
            results.append({
                "name": name,
                "address": address,
                "lat": el_lat,
                "lng": el_lng,
                "distance": f"{dist_km:.1f} km",
                "phone": phone,
                "open_now": True if opening_hours else False,
                "opening_hours": opening_hours,
                "rating": 4.0,
                "dist_val": dist_km
            })

        results.sort(key=lambda x: x["dist_val"])
        for r in results:
            del r["dist_val"]

        return {"results": results[:15], "using_sample_data": False}

    except Exception as e:
        return {"results": [], "error": f"Overpass API Error: {str(e)}", "using_sample_data": False}

@router.get("/search-address")
async def search_address(
    district: str = Query("", description="District name"),
    village: str = Query("", description="Village name"),
    pincode: str = Query("", description="Pincode"),
):
    """
    Geocode manual address details (district, village, pincode) to lat/lng coordinates.
    """
    import urllib.parse
    import httpx
    
    parts = []
    if village:
        parts.append(village)
    if district:
        parts.append(district)
    if pincode:
        parts.append(pincode)
    parts.append("Karnataka")
    parts.append("India")
    
    query_str = ", ".join([p.strip() for p in parts if p.strip()])
    
    nominatim_url = f"https://nominatim.openstreetmap.org/search?q={urllib.parse.quote(query_str)}&format=json&limit=1"
    headers = {"User-Agent": "PashuCareApp/1.0"}
    
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(nominatim_url, headers=headers, timeout=15.0)
            data = resp.json()
            
        if data:
            lat = float(data[0]["lat"])
            lng = float(data[0]["lon"])
            display_name = data[0]["display_name"]
            return {"lat": lat, "lng": lng, "display_name": display_name, "success": True}
        else:
            return {
                "lat": 12.9716, 
                "lng": 77.5946, 
                "display_name": "Bengaluru, Karnataka, India", 
                "success": False, 
                "error": "Address coordinates not found."
            }
    except Exception as e:
        return {
            "lat": 12.9716, 
            "lng": 77.5946, 
            "display_name": "Bengaluru, Karnataka, India", 
            "success": False, 
            "error": str(e)
        }

@router.get("/config")
async def get_maps_config():
    """Return map provider configuration."""
    return {"provider": "osm"}
