from fastapi import APIRouter

from api.endpoints import grpc, testing


api_router = APIRouter()

api_router.include_router(grpc.router, prefix="/grpc", tags=["grpc"])
api_router.include_router(testing.router, prefix="/testing", tags=["testing"])
