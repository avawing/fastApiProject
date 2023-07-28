from fastapi import FastAPI
from api import usersRoute, database
app = FastAPI()

app.include_router(usersRoute.router)

database.Base.metadata.create_all(bind=database.engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

