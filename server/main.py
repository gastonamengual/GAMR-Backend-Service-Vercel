from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.api.api import router

app = FastAPI()
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "access the /detect_objects endpoint"}
