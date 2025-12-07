import uvicorn
from faker import Faker


from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse

app = FastAPI()
faker = Faker()

@app.get("/")
async def read_root(request: Request):
    return RedirectResponse(f"{request.url}docs")


@app.get("/name")
async def get_name():
    return (f"Name: {faker.name()} Date: {faker.date()}")

@app.get("/address")
async def get_address():
    return (f"\nAddress: {faker.address()}")

