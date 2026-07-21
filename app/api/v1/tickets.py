from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def list_tickets() -> dict[str, list]:
    return {"tickets": []}