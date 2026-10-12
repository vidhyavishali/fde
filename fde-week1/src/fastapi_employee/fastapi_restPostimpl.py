from fastapi import APIRouter
from datasource import employees  # Import the employees list from the other file
router = APIRouter()

@router.post("/employees")
def add_employee(employee: dict):
    employees.append(employee)
    return {"message": "Employee added successfully", "employee": employee}