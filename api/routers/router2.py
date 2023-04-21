from fastapi import APIRouter

router2 = APIRouter()


@router2.get("/router2_endpoint")
async def router2_endpoint():
    return {"message": "Hello from router2!"}
