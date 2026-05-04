
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from IPython.display import display, Markdown
from fastapi import FastAPI,Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from data.employees import Employee
from database.database import  Employee as DBEmployee, Base

import os


db_url="postgresql://postgres:123456Az@localhost:5432/employees"
engine = create_engine(db_url)
Session = sessionmaker(autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

load_dotenv(override=True)  
web_search = TavilySearch(tavily_api_key=os.getenv("TAVILY_API")) 
mcp=FastMCP(name="mcp_server", host="localhost", port=2400)
app = FastAPI()


employees = [
    Employee(id=1, name="Mamadou Diallo", email="mamadou.diallo@example.com", position="Software Engineer", department="Engineering", salairy=90000, seniority="Mid-level", telephone=None, city="Dakar", country="Senegal"),
    Employee(id=2, name="Aminata Ndiaye", email="aminata.ndiaye@example.com", position="Product Manager", department="Product", salairy=95000, seniority="Senior", telephone=None, city="Dakar", country="Senegal"),
    Employee(id=3, name="Cheikh Fall", email="cheikh.fall@example.com", position="Data Scientist", department="Data Science", salairy=85000, seniority="Mid-level", telephone=None, city="Thiès", country="Senegal"),
    Employee(id=4, name="Fatou Diop", email="fatou.diop@example.com", position="UX Designer", department="Design", salairy=80000, seniority="Junior", telephone=None, city="Saint-Louis", country="Senegal"),
    Employee(id=5, name="Ousmane Sarr", email="ousmane.sarr@example.com", position="DevOps Engineer", department="Engineering", salairy=92000, seniority="Mid-level", telephone=None, city="Dakar", country="Senegal"),
    Employee(id=6, name="Mariama Ba", email="mariama.ba@example.com", position="Sales Associate", department="Sales", salairy=70000, seniority="Junior", telephone=None, city="Kaolack", country="Senegal"),
    Employee(id=7, name="Ibrahima Gueye", email="ibrahima.gueye@example.com", position="HR Specialist", department="Human Resources", salairy=75000, seniority="Mid-level", telephone=None, city="Dakar", country="Senegal"),
    Employee(id=8, name="Ndèye Khady Seck", email="khady.seck@example.com", position="Marketing Coordinator", department="Marketing", salairy=65000, seniority="Junior", telephone=None, city="Rufisque", country="Senegal"),
    Employee(id=9, name="Babacar Faye", email="babacar.faye@example.com", position="IT Support Specialist", department="IT", salairy=60000, seniority="Junior", telephone=None, city="Dakar", country="Senegal"),
    Employee(id=10, name="Moustapha Kane", email="moustapha.kane@example.com", position="Financial Analyst", department="Finance", salairy=70000, seniority="Mid-level", telephone=None, city="Ziguinchor", country="Senegal"),
    Employee(id=11, name="Seynabou Sow", email="seynabou.sow@example.com", position="Legal Counsel", department="Legal", salairy=85000, seniority="Senior", telephone=None, city="Dakar", country="Senegal"),
    Employee(id=12, name="Alioune Ndour", email="alioune.ndour@example.com", position="Backend Developer", department="Engineering", salairy=88000, seniority="Mid-level", telephone=None, city="Thiès", country="Senegal"),
    Employee(id=13, name="Awa Cissé", email="awa.cisse@example.com", position="Frontend Developer", department="Engineering", salairy=87000, seniority="Mid-level", telephone=None, city="Dakar", country="Senegal"),
    Employee(id=14, name="Serigne Mbaye", email="serigne.mbaye@example.com", position="QA Engineer", department="Engineering", salairy=78000, seniority="Junior", telephone=None, city="Touba", country="Senegal"),
    Employee(id=15, name="Pape Diagne", email="pape.diagne@example.com", position="System Administrator", department="IT", salairy=82000, seniority="Mid-level", telephone=None, city="Dakar", country="Senegal"),
    Employee(id=16, name="Astou Ndiaye", email="astou.ndiaye@example.com", position="Business Analyst", department="Business", salairy=83000, seniority="Mid-level", telephone=None, city="Dakar", country="Senegal"),
    Employee(id=17, name="Lamine Ba", email="lamine.ba@example.com", position="Network Engineer", department="IT", salairy=81000, seniority="Mid-level", telephone=None, city="Saint-Louis", country="Senegal"),
    Employee(id=18, name="Khady Fall", email="khady.fall@example.com", position="Content Manager", department="Marketing", salairy=72000, seniority="Junior", telephone=None, city="Dakar", country="Senegal"),
    Employee(id=19, name="Moussa Sow", email="moussa.sow@example.com", position="Security Engineer", department="IT", salairy=90000, seniority="Senior", telephone=None, city="Thiès", country="Senegal"),
    Employee(id=20, name="Fatoumata Diallo", email="fatoumata.diallo@example.com", position="Project Manager", department="Management", salairy=95000, seniority="Senior", telephone=None, city="Dakar", country="Senegal")
]

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

def add_employees_to_db():
    db = next(get_db())
    for emp in employees:
        db_employee = DBEmployee(
            id=emp.id,
            name=emp.name,
            email=emp.email,
            position=emp.position,
            department=emp.department,
            salairy=emp.salairy,
            seniority=emp.seniority,
            telephone=emp.telephone,
            city=emp.city,
            country=emp.country
        )
        db.add(db_employee)
    db.commit()

@mcp.tool(name="search", description="Search the web for information")
@app.get("/search")
def search(query):
    res= web_search.invoke(query)
    return res


@mcp.tool(name="list_employees", description="List all employees")
@app.get("/employees")
def list_employees():
    db = next(get_db())
    employees = db.query(DBEmployee).all()
    return employees

@app.get("/employees/{employee_email}")
@mcp.tool(name="get_employee_by_email", description="Get employee details by email")
def get_employee_by_email(employee_email: str):
    db = next(get_db())
    employee = db.query(DBEmployee).filter(DBEmployee.email == employee_email).first()
    return employee

@app.get("/employees/name/{employee_name}")
@mcp.tool(name="get_employee_by_name", description="Get employee details by name")
def get_employee_by_name(employee_name: str):
    db= next(get_db())
    db_employee = db.query(DBEmployee).filter(DBEmployee.name == employee_name).first()
    if db_employee:
        return db_employee
    return None

@app.post("/employees")
@mcp.tool(name="add_employee", description="Add a new employee")
def add_employee(employee: Employee):
    db = next(get_db())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

@app.delete("/employees/name/{name}")
@mcp.tool(name="delete_employee_by_name", description="Delete an employee by name")
def delete_employee_by_name(name: str):
    db = next(get_db())
    employee = db.query(DBEmployee).filter(DBEmployee.name == name).first()
    if employee:
        db.delete(employee)
        db.commit()
        return {"message": f"Employee with name {name} deleted"}
    return {"message": "Employee not found"}

@app.delete("/employees/{employee_email}")
@mcp.tool(name="delete_employee_by_email", description="Delete an employee by email")
def delete_employee_by_email(employee_email: str):
    db = next(get_db())
    employee = db.query(DBEmployee).filter(DBEmployee.email == employee_email).first()
    if employee:
        db.delete(employee)
        db.commit()
        return {"message": f"Employee with email {employee_email} deleted"}
    return {"message": "Employee not found"}

@app.put("/employees/{employee_email}")
@mcp.tool(name="update_employee_by_email", description="Update employee details by email")
def update_employee_by_email(employee_email: str, updated_employee: Employee):
    db = next(get_db())
    employee = db.query(DBEmployee).filter(DBEmployee.email == employee_email).first()
    if employee:
        for key, value in updated_employee.dict().items():
            setattr(employee, key, value)
        db.commit()
        db.refresh(employee)
        return employee
    return None

if __name__ == "__main__":
    add_employees_to_db()
    mcp.run(transport="streamable-http")