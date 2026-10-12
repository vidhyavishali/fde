from fastapi import APIRouter
from datasource import employees  # Import the employees list from the other file
router = APIRouter()  # router initialization



@router.get("/employees")
def get_employees():
    return employees

@router.get("/employees/{employee_id}")
def get_employee_by_id(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return {"error": "Employee not found"}
