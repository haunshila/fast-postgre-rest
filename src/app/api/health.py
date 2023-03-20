from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health():
    # some async operation could happen here
    return {"health": "Ok!!!"}