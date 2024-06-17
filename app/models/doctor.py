from sqlmodel import Field, Relationship, SQLModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .video import Video

class DoctorBase(SQLModel):
    name: str = Field(nullable=False)
    specialty: str | None = Field()
    location: str | None = Field()
    picture_url: str | None = Field()
    featured_doctor: bool | None = Field(default=False)

class DoctorCreate(DoctorBase):
    pass

class DoctorUpdate(DoctorBase):
    pass

class Doctor(DoctorBase, table=True):
    id: int = Field(primary_key=True, nullable=False)
    videos:"Video" = Relationship(back_populates="doctor")