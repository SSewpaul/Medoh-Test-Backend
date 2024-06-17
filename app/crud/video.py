from models.video import Video, VideoCreate
from sqlmodel import Session, text, select, and_
from fastapi.encoders import jsonable_encoder

class CRUDVideo():
    def create_video(self, session:Session, video_obj: VideoCreate) -> Video:
        video_data = jsonable_encoder(video_obj)
        db_obj = Video(**video_data)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj
    
    def lookup_titles(self, session:Session, query: list[str]) -> list[Video]:
        filter_list = [Video.title.contains(word) for word in query]
        # statement = text(f"SELECT * FROM Video WHERE title ~* '{query_arr}'")
        statement = select(Video).filter(and_(*filter_list))
        res = session.exec(statement)
        return res
    
    def get_featured_videos(self, session: Session) -> list[Video]:
        statement = select(Video).filter(Video.featured_video == True)
        res = session.exec(statement)
        return res

video = CRUDVideo()