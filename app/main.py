from fastapi import FastAPI
from routes.router import api_router

app = FastAPI()

app.include_router(api_router)