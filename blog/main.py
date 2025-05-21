from  fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
import models
import schemas
from sqlalchemy.orm import Session
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog")
def create_blog(request:schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {"data": f"blog is created with title as {new_blog.title} and body as {new_blog.body}"}