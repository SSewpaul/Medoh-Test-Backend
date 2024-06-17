from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from fastapi.encoders import jsonable_encoder

import crud
from models.video import Video, VideoCreate
from db import get_session

router = APIRouter()

@router.post("/", response_model=Video)
def create_video(*, session: Session = Depends(get_session), video_obj: VideoCreate) -> any:
    video_data = jsonable_encoder(video_obj)
    doctor = crud.doctor.get_doctor_by_id(session, video_data.get('doctor_id'))

    if not doctor:
        raise HTTPException(status_code=404, detail='Doctor does not exist')
    
    video = crud.video.create_video(session, video_obj)
    return video

@router.get("/search/{query}", response_model=list[Video])
def search(*, session: Session = Depends(get_session), query: str):

    if not query:
        return []

    query_words = [word for word in query.split()]
    titles_obj = crud.video.lookup_titles(session, query_words)
    search_results = []
    for val in titles_obj:
        search_results.append(Video(
            title= val.title,
            thumbnail_url= val.thumbnail_url,
            video_url= val.video_url,
            video_type= val.video_type,
            doctor_id= val.doctor_id,
            popular_video= val.popular_video,
            featured_video= val.featured_video,
            id= val.id
        ))

    return search_results

@router.get("/featured_videos", response_model=list[Video])
def get_featured_videos(*, session: Session = Depends(get_session)):
    titles_obj = crud.video.get_featured_videos(session)
    search_results = []
    for val in titles_obj:
        search_results.append(Video(
            title= val.title,
            thumbnail_url= val.thumbnail_url,
            video_url= val.video_url,
            video_type= val.video_type,
            doctor_id= val.doctor_id,
            popular_video= val.popular_video,
            featured_video= val.featured_video,
            id= val.id
        ))

    return search_results