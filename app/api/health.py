from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def healthCheck():
    return {"message": "success"}
