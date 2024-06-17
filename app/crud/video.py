from models.video import Video, VideoCreate
from sqlmodel import Session, text
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
        query_arr = ''.join(f"{word}|" for word in query)
        query_arr = (query_arr[:-1])
        statement = text(f"SELECT * FROM Video WHERE title ~* '{query_arr}'")
        res = session.exec(statement)
        return res

video = CRUDVideo()