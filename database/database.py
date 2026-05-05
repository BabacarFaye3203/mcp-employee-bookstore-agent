
from sqlalchemy import  Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"

    id= Column(Integer, primary_key=True, autoincrement=True)
    name= Column(String(100),nullable=False)
    email= Column(String(100),nullable=False, unique=True)
    position= Column(String(100),nullable=False)
    department= Column(String(100),nullable=False)
    salairy= Column(Float,nullable=False)
    seniority= Column(String(100),nullable=False)
    telephone= Column(String(20),nullable=True)
    city= Column(String(100),nullable=True)
    country= Column(String(100),nullable=True)

    def __init__(self, id=None, name=None, email=None, position=None, department=None, salairy=None, seniority=None, telephone=None, city=None, country=None):
        self.id = id
        self.name = name
        self.email = email
        self.position = position
        self.department = department
        self.salairy = salairy
        self.seniority = seniority
        self.telephone = telephone
        self.city = city
        self.country = country
