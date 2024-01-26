from fastapi import FastAPI

from app.fastapi import hello

app = FastAPI()

hello()
