from fastapi import FastAPI

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

def calculate(a, b):
    return a + b


@app.get("/calculate")
def get_result(a: float, b: float):
    result = calculate(a, b)
    return {"result": result}

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
def home():
    return FileResponse("index.html")