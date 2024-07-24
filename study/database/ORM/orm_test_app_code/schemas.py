from pydantic import BaseModel
from datetime import date

class StudentBase(BaseModel):
    sid: int
    name: str
    grade: int
    birth: date
    email: str
    auth: int

class Student(StudentBase):
    gender: str | None = None
    phone: str | None = None
    nickname: str | None = None

    class Config:
        from_attributes = True # orm_mode : pydantic V1. now V2

class StudentCreate(StudentBase):
    gender: str | None = None
    phone: str | None = None
    nickname: str | None = None
    password: str