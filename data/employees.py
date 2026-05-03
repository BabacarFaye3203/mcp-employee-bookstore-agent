from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    position: str
    department: str
    salairy: float
    seniority: str
