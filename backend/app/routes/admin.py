"""Admin routes — dashboard statistics, user management."""

from fastapi import APIRouter, Depends, HTTPException, status
from ..middleware.auth import get_current_admin
from ..database import get_db

router = APIRouter(prefix="/api/admin", tags=["Admin"])

@router.get("/dashboard")
async def get_dashboard_stats(admin_user=Depends(get_current_admin)):
    """Get overall system statistics for the admin dashboard."""
    db = get_db()
    if db is None:
        raise HTTPException(status_code=503, detail="Database not available.")

    # Total users
    total_users = await db.users.count_documents({})

    # Total detections
    total_detections = await db.detections.count_documents({})

    # Recent activity (latest 5 users, latest 5 detections)
    recent_users_cursor = db.users.find({}, {"password": 0}).sort("created_at", -1).limit(5)
    recent_users = []
    async for u in recent_users_cursor:
        u["_id"] = str(u["_id"])
        recent_users.append(u)

    recent_detections_cursor = db.detections.find({}).sort("timestamp", -1).limit(5)
    recent_detections = []
    async for d in recent_detections_cursor:
        d["_id"] = str(d.pop("_id", ""))
        recent_detections.append(d)

    return {
        "statistics": {
            "total_users": total_users,
            "total_detections": total_detections,
            "total_chatbot_conversations": "Not tracked", # Assuming not tracked in DB
            "system_health": "Online"
        },
        "recent_users": recent_users,
        "recent_detections": recent_detections
    }
