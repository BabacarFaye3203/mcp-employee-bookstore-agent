from pydantic import BaseModel
from typing import  Optional

class Employee(BaseModel):
    id: int
    name: str
    email: str
    position: str
    department: str
    salairy: float
    seniority: str
    telephone: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
