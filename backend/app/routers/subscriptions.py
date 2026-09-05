from fastapi import APIRouter

router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])


@router.get("/")
def list_subscriptions():
    # TODO: return detected subscriptions with usage/inactivity flags
    return []
