from fastapi import APIRouter

router = APIRouter(prefix="/scan", tags=["scan"])


@router.post("/run")
def run_scan():
    # TODO: pull last 90 days of Gmail receipts and extract subscriptions
    return {"todo": "run gmail scan"}
