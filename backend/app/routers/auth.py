from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/login")
def login():
    # TODO: kick off Gmail OAuth flow
    return {"todo": "gmail oauth login"}

@router.get("/callback")
def callback():
    # TODO: handle OAuth callback and store tokens
    return {"todo": "gmail oauth callback"}
