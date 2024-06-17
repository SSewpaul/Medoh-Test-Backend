from models.doctor import Doctor, DoctorCreate
from sqlmodel import Session, select
from fastapi.encoders import jsonable_encoder

class CRUDDoctor():
    def create_doctor(self, session:Session, doctor_obj: DoctorCreate) -> Doctor:
        doctor_data = jsonable_encoder(doctor_obj)
        db_obj = Doctor(**doctor_data)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj
    
    def get_doctor_by_id(self, session:Session, id: int) -> Doctor:
        doctor = session.get(Doctor, id)
        return doctor
    
    def get_featured_doctor(self, session:Session) -> list[Doctor]:
        statement = select(Doctor)
        res = session.exec(statement)
        return res

doctor = CRUDDoctor()