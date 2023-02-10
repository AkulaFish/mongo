from fastapi import FastAPI, Body, Response

from db.db_connection import db, employees
from db.schemas import Employee

app = FastAPI()


@app.get("/greeting")
async def greeting():
    return "Hello from mongo!"


@app.post("/api/v1/create-employee")
async def create_employee(user: Employee = Body()):
    employee = employees.insert_one(user.dict())
    return Response("Item created successfully")
