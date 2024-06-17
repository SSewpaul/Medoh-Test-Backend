from fastapi import APIRouter
from . import doctor, video

api_router = APIRouter()

api_router.include_router(doctor.router, prefix="/doctor", tags=['doctor'])
api_router.include_router(video.router, prefix="/video", tags=['video'])