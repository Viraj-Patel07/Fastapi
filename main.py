from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/blogs")
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs from the database"}
    else:
        return {"data": f"{limit} blogs from the database"}
    

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    
    def dict(self): 
        return super().dict(exclude_unset=True)
    
@app.post("/blog")
def create_blog(blog: Blog):
    return {"data":f"blog is created with title as {blog.title} and body as {blog.body}"}

        
@app.get("/blog/unpublished")
def unpublished():
    return {"data":"No published blogs"}

@app.get("/blog/{id}")
def show(id: int):
    return {"data":id}

@app.get("/blog/{id}/comments")
def comments(id: int):
    return {"data":{1,2,3,4,5,6,7,8,9,10}}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=9000)

