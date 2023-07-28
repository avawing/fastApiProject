from fastapi import FastAPI
from api import usersRoute
app = FastAPI()

app.include_router(usersRoute.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

