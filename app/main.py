import uvicorn
from fastapi import FastAPI

from app.database import lifespan

app = FastAPI(lifespan=lifespan)


@app.get("/health")
async def root():
    return {"status": "up!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
