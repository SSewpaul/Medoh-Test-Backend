from fastapi import APIRouter, Depends
from sqlmodel import Session

import crud
from models.doctor import Doctor, DoctorCreate
from db import get_session

router = APIRouter()

@router.post("/", response_model=Doctor)
def create_doctor(*, session: Session = Depends(get_session), doctor_obj: DoctorCreate) -> Doctor:
    doctor = crud.doctor.create_doctor(session, doctor_obj)
    return doctor

@router.get("/details/{doctor_id}", response_model=Doctor)
def get_doctor(*, session: Session = Depends(get_session), doctor_id: int) -> Doctor:
    doctor = crud.doctor.get_doctor_by_id(session, doctor_id)
    return doctor

@router.get("/featured_doctors")
def get_featured_doctor(*, session: Session = Depends(get_session)):
    doctors_obj = crud.doctor.get_featured_doctor(session)
    doctors = []
    for val in doctors_obj:
        doctors.append(Doctor(
            name = val.name,
            specialty = val.specialty,
            location = val.location,
            picture_url = val.picture_url,
            featured_doctor = val.featured_doctor,
            id = val.id
        ))

    return doctors