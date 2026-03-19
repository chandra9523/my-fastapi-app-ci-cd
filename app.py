from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CI/CD pipeline working!"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}