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

@router.get("/{doctor_id}", response_model=Doctor)
def get_doctor(*, session: Session = Depends(get_session), doctor_id: int) -> Doctor:
    doctor = crud.doctor.get_doctor_by_id(session, doctor_id)
    return doctor