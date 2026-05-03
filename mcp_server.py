
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from IPython.display import display, Markdown
from fastapi import FastAPI
from data.employees import Employee
import os

employees=[
    Employee(id=1, name="Alice", position="Software Engineer", department="Engineering", salairy=90000, seniority="Mid-level"),
    Employee(id=2, name="Bob", position="Product Manager", department="Product", salairy=95000, seniority="Senior"),
    Employee(id=3, name="Charlie", position="Data Scientist", department="Data Science", salairy=85000, seniority="Mid-level"),
    Employee(id=4, name="David", position="UX Designer", department="Design", salairy=80000, seniority="Junior"),
    Employee(id=5, name="Eve", position="DevOps Engineer", department="Engineering", salairy=92000, seniority="Mid-level")
]

load_dotenv(override=True)  
web_search = TavilySearch(tavily_api_key=os.getenv("TAVILY_API")) 
mcp=FastMCP(name="mcp_server", host="localhost", port=2400)
app = FastAPI()

@mcp.tool(name="search", description="Search the web for information")
@app.get("/search")
def search(query):
    res= web_search.invoke(query)
    return res


@mcp.tool(name="list_employees", description="List all employees")
@app.get("/employees")
def list_employees():
    return employees

@app.get("/employees/{employee_id}")
@mcp.tool(name="get_employee", description="Get employee details by ID")
def get_employee_by_id(employee_id: int):
    for emp in employees:
        if emp.id == employee_id:
            return emp
    return None

@app.get("/employees/name/{employee_name}")
@mcp.tool(name="get_employee_by_name", description="Get employee details by name")
def get_employee_by_name(employee_name: str):
    for emp in employees:
        if emp.name.lower() == employee_name.lower():
            return emp
    return None

@app.post("/employees")
@mcp.tool(name="add_employee", description="Add a new employee")
def add_employee(employee: Employee):
    employees.append(employee)
    return employee

def delete_employee_by_name(name: str):
    global employees
    employees = [emp for emp in employees if emp.name != name]
    return {"message": f"Employee with name {name} deleted"}

@app.delete("/employees/{employee_id}")
@mcp.tool(name="delete_employee_by_name", description="Delete an employee by name")
def delete_employee(employee_name: str):
    return delete_employee_by_name(employee_name)

@mcp.tool(name="get_employee_by_name", description="Get employee details by name")
def get_employee_by_name(name: str):
    for emp in employees:
        if emp.name.lower() == name.lower():
            return emp
    return None

if __name__ == "__main__":
    mcp.run(transport="streamable-http")