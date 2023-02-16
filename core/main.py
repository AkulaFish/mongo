from fastapi import FastAPI, Body, Response
from bson.objectid import ObjectId
from bson.errors import InvalidId

from db.db_connection import employees
from db.schemas import Employee

app = FastAPI()


@app.get("/greeting")
async def greeting():
    return "Hello from mongo!"


@app.post("/api/v1/employees")
async def create_employee(user: Employee = Body()) -> Response:
    await employees.insert_one(user.dict())
    return Response("Employee created successfully", status_code=200)


@app.get("/api/v1/employees/{employee_id}")
async def get_employee(employee_id: str) -> Employee | dict:
    try:
        result = await employees.find_one({"_id": ObjectId(str(employee_id))})
        return Employee.parse_obj(dict(result))
    except (InvalidId, TypeError):
        return {"detail": "Invalid object id or object not found"}


@app.delete("/api/v1/employees/{employee_id}", status_code=200)
async def delete_employee(employee_id: str) -> dict:
    try:
        await employees.delete_one({"_id": ObjectId(employee_id)})
    except (InvalidId, TypeError):
        return {"detail": "Invalid object id or object not found"}

    return {"detail": "Employee deleted successfully"}
