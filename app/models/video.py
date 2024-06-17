from sqlmodel import Field, Relationship, SQLModel
from .doctor import Doctor

class VideoBase(SQLModel):
    title: str = Field(nullable=False, index=True)
    thumbnail_url: str | None = Field()
    video_url: str = Field()
    video_type: str = Field()
    doctor_id: int = Field(foreign_key="doctor.id")
    popular_video: bool = Field(default= False)
    featured_video: bool = Field(default=False)

class VideoCreate(VideoBase):
    pass

class VideoUpdate(VideoBase):
    pass

class Video(VideoBase, table=True):
    id: int = Field(primary_key=True, nullable=False)
    doctor:Doctor = Relationship(back_populates="videos")