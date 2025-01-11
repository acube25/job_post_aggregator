from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.utils.db import get_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Post Aggregator!"}

@app.get("/test-db/")
def test_database(db: Session = Depends(get_db)):
    return {"message": "database connection successful!"}