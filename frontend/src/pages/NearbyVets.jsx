import React, { useState, useEffect } from "react";
import { useLanguage } from "../context/LanguageContext";
import { useAuth } from "../context/AuthContext";
import api from "../services/api";
import { MapPin, Phone, Clock, Star, Compass, Navigation, Info, AlertTriangle, Search } from "lucide-react";
import { motion } from "framer-motion";

// React Leaflet imports
import { MapContainer, TileLayer, Marker, Popup, Polyline, useMap } from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

// Recenter Component to programmatically pan/zoom map on coordinate update
const RecenterMap = ({ lat, lng }) => {
  const map = useMap();
  useEffect(() => {
    map.setView([lat, lng], 13);
  }, [lat, lng, map]);
  return null;
};

// Custom icons using inline SVG to avoid Vite bundler asset paths errors
const userIcon = L.divIcon({
  html: `<div style="background-color: #3b82f6; width: 14px; height: 14px; border-radius: 50%; border: 3px solid white; box-shadow: 0 0 12px rgba(59, 130, 246, 0.7); margin: 0 auto;"></div>`,
  className: "custom-user-marker",
  iconSize: [14, 14],
  iconAnchor: [7, 7]
});

const vetIcon = L.divIcon({
  html: `<div style="color: #ef4444;"><svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg></div>`,
  className: "custom-vet-marker",
  iconSize: [28, 28],
  iconAnchor: [14, 28]
});

const selectedVetIcon = L.divIcon({
  html: `<div style="color: #10b981;"><svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg></div>`,
  className: "custom-vet-marker-selected",
  iconSize: [36, 36],
  iconAnchor: [18, 36]
});

const NearbyVets = () => {
  const { t } = useLanguage();
  const { user } = useAuth();

  const [location, setLocation] = useState({ lat: 12.9716, lng: 77.5946 }); // Default Bangalore
  const [loadingLoc, setLoadingLoc] = useState(false);
  const [vets, setVets] = useState([]);
  const [loadingVets, setLoadingVets] = useState(false);
  const [error, setError] = useState("");
  const [isDemoData, setIsDemoData] = useState(false);
  const [selectedVet, setSelectedVet] = useState(null);
  
  // Geolocation access state
  const [locAccessDenied, setLocAccessDenied] = useState(false);

  // Manual fallback search inputs
  const [district, setDistrict] = useState("");
  const [village, setVillage] = useState("");
  const [pincode, setPincode] = useState("");

  // Fetch location on mount
  useEffect(() => {
    getUserLocation();
  }, []);

  // Fetch clinics when location changes
  useEffect(() => {
    fetchNearbyVets();
  }, [location]);

  const getUserLocation = () => {
    if (!navigator.geolocation) {
      setError("Geolocation is not supported by your browser.");
      setLocAccessDenied(true);
      return;
    }

    setLoadingLoc(true);
    setError("");
    setLocAccessDenied(false);

    navigator.geolocation.getCurrentPosition(
      (position) => {
        setLocation({
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        });
        setLoadingLoc(false);
      },
      (err) => {
        console.warn("Geolocation permission denied or error. Using fallback.", err);
        setError(t("unableToAccessLocation"));
        setLocAccessDenied(true);
        setLoadingLoc(false);
      },
      { timeout: 10000 }
    );
  };

  const fetchNearbyVets = async () => {
    setLoadingVets(true);
    try {
      const response = await api.get("/api/vets/nearby", {
        params: { lat: location.lat, lng: location.lng },
      });
      if (response.data.error && response.data.results?.length === 0) {
        setError(response.data.error);
        setVets([]);
        setSelectedVet(null);
      } else {
        const results = response.data.results || [];
        setVets(results);
        setIsDemoData(response.data.using_sample_data || false);
        // Default select the nearest hospital
        if (results.length > 0) {
          setSelectedVet(results[0]);
        } else {
          setSelectedVet(null);
        }
      }
    } catch (err) {
      console.error(err);
      setError(t("fetchVetsError"));
    } finally {
      setLoadingVets(false);
    }
  };

  const handleManualSearch = async (e) => {
    e.preventDefault();
    if (!district && !village && !pincode) return;

    setLoadingVets(true);
    setError("");
    try {
      const response = await api.get("/api/vets/search-address", {
        params: { district, village, pincode }
      });
      if (response.data.success) {
        setLocation({
          lat: response.data.lat,
          lng: response.data.lng
        });
      } else {
        setError(response.data.error || t("noVetsFound"));
        setLoadingVets(false);
      }
    } catch (err) {
      console.error("Geocoding failed:", err);
      setError(t("fetchVetsError"));
      setLoadingVets(false);
    }
  };

  return (
    <div className="bg-slate-950 text-white min-h-screen py-10 px-4 sm:px-6 lg:px-8">
      <div className="max-w-6xl mx-auto space-y-8">
        {/* Header */}
        <div className="text-center space-y-2">
          <h1 className="text-3xl sm:text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-teal-400">
            {t("nearbyVetHospital")}
          </h1>
          <p className="text-slate-400 text-sm max-w-md mx-auto">
            {t("nearbyVetsDesc")}
          </p>
        </div>

        {error && (
          <div className="bg-red-500/10 border border-red-500/20 rounded-xl p-4 flex items-center space-x-3 text-red-400 text-sm">
            <AlertTriangle className="w-5 h-5 shrink-0" />
            <span>{error}</span>
          </div>
        )}

        {isDemoData && (
          <div className="bg-amber-500/10 border border-amber-500/20 rounded-xl p-4 flex items-center space-x-3 text-amber-400 text-sm">
            <AlertTriangle className="w-5 h-5 shrink-0" />
            <span>{t("mockAlert")}</span>
          </div>
        )}

        {/* Fallback Location Input Panel */}
        {locAccessDenied && (
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-slate-900 border border-slate-800 rounded-2xl p-6 max-w-xl mx-auto space-y-4"
          >
            <div className="flex items-center space-x-2 text-amber-400">
              <AlertTriangle className="w-5 h-5" />
              <h2 className="font-extrabold text-sm uppercase tracking-wider">
                {t("unableToAccessLocation")}
              </h2>
            </div>
            <p className="text-xs text-slate-400 leading-relaxed">
              To locate veterinary hospitals, please input your village, district name, or postal pincode below:
            </p>

            <form onSubmit={handleManualSearch} className="grid grid-cols-1 sm:grid-cols-3 gap-3">
              <div>
                <input
                  type="text"
                  placeholder={t("village")}
                  value={village}
                  onChange={(e) => setVillage(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 text-xs text-slate-200 focus:outline-none focus:border-emerald-500/50"
                />
              </div>
              <div>
                <input
                  type="text"
                  placeholder={t("district")}
                  value={district}
                  onChange={(e) => setDistrict(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 text-xs text-slate-200 focus:outline-none focus:border-emerald-500/50"
                />
              </div>
              <div>
                <input
                  type="text"
                  placeholder={t("pincode")}
                  value={pincode}
                  onChange={(e) => setPincode(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 text-xs text-slate-200 focus:outline-none focus:border-emerald-500/50"
                />
              </div>
              <button
                type="submit"
                disabled={loadingVets || (!district && !village && !pincode)}
                className="sm:col-span-3 w-full py-3 bg-emerald-600 hover:bg-emerald-700 disabled:bg-slate-800 disabled:text-slate-500 disabled:cursor-not-allowed text-white font-bold rounded-xl transition flex items-center justify-center space-x-2 text-sm cursor-pointer shadow-lg shadow-emerald-950/20"
              >
                <Search className="w-4 h-4" />
                <span>{loadingVets ? "Searching..." : t("manualSearchBtn")}</span>
              </button>
            </form>

            <div className="text-center pt-2">
              <button
                onClick={getUserLocation}
                className="text-xs text-emerald-450 hover:underline font-bold transition cursor-pointer"
              >
                Retry GPS Geolocation
              </button>
            </div>
          </motion.div>
        )}

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* List panel */}
          <div className="lg:col-span-1 space-y-4">
            <button
              onClick={getUserLocation}
              disabled={loadingLoc}
              className="w-full py-3 bg-slate-900 border border-slate-800 hover:bg-slate-850 rounded-xl font-bold flex items-center justify-center space-x-2 text-emerald-400 transition cursor-pointer"
            >
              <Navigation className="w-5 h-5" />
              <span>{loadingLoc ? t("locating") : t("getLocationBtn")}</span>
            </button>

            {loadingVets ? (
              <div className="flex flex-col items-center justify-center py-20 space-y-3">
                <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-emerald-500" />
                <span className="text-sm text-slate-400">{t("searchingVets")}</span>
              </div>
            ) : vets.length === 0 ? (
              <div className="text-center py-12 bg-slate-900 border border-slate-800 rounded-xl text-slate-450">
                <Compass className="w-12 h-12 mx-auto mb-2 text-slate-600" />
                <p className="text-sm">{t("noVetsFound")}</p>
              </div>
            ) : (
              <div className="space-y-4 max-h-[500px] overflow-y-auto pr-2 custom-scrollbar">
                {vets.map((vet, idx) => {
                  const isSelected = selectedVet && selectedVet.name === vet.name;
                  return (
                    <motion.div
                      key={idx}
                      initial={{ opacity: 0, y: 10 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: idx * 0.05 }}
                      onClick={() => setSelectedVet(vet)}
                      className={`cursor-pointer border p-4 rounded-xl space-y-3 transition ${
                        isSelected
                          ? "bg-slate-900 border-emerald-500/50 shadow-lg shadow-emerald-950/20"
                          : "bg-slate-900 border-slate-800 hover:border-slate-700"
                      }`}
                    >
                      <div className="flex justify-between items-start">
                        <h3 className={`font-bold ${isSelected ? "text-emerald-400" : "text-slate-200"}`}>
                          {vet.name}
                        </h3>
                        <div className="flex items-center text-amber-400 text-xs shrink-0 ml-2">
                          <Star className="w-3.5 h-3.5 fill-current mr-1" />
                          <span>{vet.rating || "4.0"}</span>
                        </div>
                      </div>

                      <div className="space-y-1.5 text-slate-400 text-xs">
                        <p className="flex items-start space-x-2">
                          <MapPin className="w-4 h-4 text-emerald-450 shrink-0 mt-0.5" />
                          <span className="line-clamp-2">{vet.address}</span>
                        </p>
                        {vet.phone && (
                          <p className="flex items-center space-x-2">
                            <Phone className="w-4 h-4 text-emerald-450 shrink-0" />
                            <a href={`tel:${vet.phone}`} className="hover:underline hover:text-emerald-400">
                              {vet.phone}
                            </a>
                          </p>
                        )}
                        <p className="flex items-center space-x-2">
                          <Clock className="w-4 h-4 text-emerald-450 shrink-0" />
                          <span className={vet.open_now ? "text-emerald-400" : "text-red-400"}>
                            {vet.open_now ? t("openNow") : t("closed")}
                          </span>
                        </p>
                      </div>

                      <div className="flex justify-between items-center pt-1.5">
                        {vet.distance && (
                          <span className="inline-block bg-slate-950 border border-slate-850 px-2 py-1 rounded text-[10px] text-slate-450 font-bold uppercase">
                            {vet.distance} away
                          </span>
                        )}
                        
                        {vet.phone && (
                          <a
                            href={`tel:${vet.phone}`}
                            className="bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-[10px] px-3 py-1.5 rounded-lg transition tracking-wide uppercase shrink-0"
                            onClick={(e) => e.stopPropagation()} // Stop selection toggle
                          >
                            Call Clinic
                          </a>
                        )}
                      </div>
                    </motion.div>
                  );
                })}
              </div>
            )}
          </div>

          {/* Map panel */}
          <div className="lg:col-span-2 space-y-4">
            <div className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden h-[560px] relative shadow-lg">
              <MapContainer
                center={[location.lat, location.lng]}
                zoom={13}
                scrollWheelZoom={true}
                style={{ height: "100%", width: "100%", zIndex: 1 }}
              >
                <TileLayer
                  attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors | Map data &copy; <a href="https://overpass-api.de?utm_source=chatgpt.com" target="_blank" rel="noopener noreferrer">Overpass API</a>'
                  url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                
                {/* User Location Marker */}
                <Marker position={[location.lat, location.lng]} icon={userIcon}>
                  <Popup>
                    <div className="text-slate-900 font-bold text-xs">Your Location</div>
                  </Popup>
                </Marker>

                {/* Veterinary Hospital Markers */}
                {vets.map((vet, idx) => {
                  const isSelected = selectedVet && selectedVet.name === vet.name;
                  return (
                    <Marker
                      key={idx}
                      position={[vet.lat, vet.lng]}
                      icon={isSelected ? selectedVetIcon : vetIcon}
                      eventHandlers={{
                        click: () => {
                          setSelectedVet(vet);
                        },
                      }}
                    >
                      <Popup>
                        <div className="text-slate-900 text-xs p-1">
                          <h4 className="font-extrabold">{vet.name}</h4>
                          <p className="text-[10px] text-slate-650 mt-0.5">{vet.address}</p>
                          {vet.phone && <p className="text-[10px] font-bold text-emerald-600 mt-1">📞 {vet.phone}</p>}
                        </div>
                      </Popup>
                    </Marker>
                  );
                })}

                {/* Distance Route Information (Polyline) */}
                {selectedVet && (
                  <Polyline
                    positions={[
                      [location.lat, location.lng],
                      [selectedVet.lat, selectedVet.lng]
                    ]}
                    color="#10b981"
                    weight={4}
                    dashArray="6, 12"
                  />
                )}

                {/* Recenter Map on coords change */}
                <RecenterMap lat={location.lat} lng={location.lng} />
              </MapContainer>
            </div>
            <div className="text-right text-[10px] text-slate-500 pr-2">
              Hospital search query provided by <a href="https://overpass-api.de?utm_source=chatgpt.com" target="_blank" rel="noopener noreferrer" className="text-emerald-500 hover:underline">Overpass API</a> &copy; OpenStreetMap contributors.
            </div>

            {/* Route Detail Card */}
            {selectedVet && (
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                className="bg-slate-900 border border-slate-800 rounded-xl p-4 flex items-center justify-between"
              >
                <div className="flex items-center space-x-3">
                  <div className="p-2.5 bg-emerald-600/10 rounded-lg text-emerald-450 border border-emerald-500/20">
                    <MapPin className="w-5 h-5 shrink-0" />
                  </div>
                  <div>
                    <h4 className="font-extrabold text-sm text-slate-200">
                      Route to {selectedVet.name}
                    </h4>
                    <p className="text-xs text-slate-400 mt-0.5">
                      Direct distance: <span className="text-emerald-400 font-bold">{selectedVet.distance}</span>
                    </p>
                  </div>
                </div>

                {selectedVet.phone && (
                  <a
                    href={`tel:${selectedVet.phone}`}
                    className="flex items-center space-x-1 bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-xs px-4 py-2.5 rounded-xl shadow-lg shadow-emerald-950/30 transition cursor-pointer"
                  >
                    <Phone className="w-4 h-4" />
                    <span>Call Clinic</span>
                  </a>
                )}
              </motion.div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default NearbyVets;
