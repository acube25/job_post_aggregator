from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.utils.db import get_db

from app.models.user import Base
from app.utils.db import engine
from app.routers import auth

Base.metadata.create_all(bind = engine)
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Post Aggregator!"}

@app.get("/test-db/")
def test_database(db: Session = Depends(get_db)):
    return {"message": "database connection successful!"}

app.include_router(auth.router)