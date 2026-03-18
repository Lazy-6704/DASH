from fastapi import FastAPI, Request, HTTPException, status
# from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import ast

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'),name='static')

templates = Jinja2Templates(directory="templates/blog")

with open("snippets.txt", "r") as file:
    Posts = ast.literal_eval(file.read())

@app.get("/", include_in_schema=False, name='home')    # include_in_schema=False -> hides the route from the documentation
@app.get("/Posts", name='Posts')    # Multiple routes can navigate to same page
def home(request:Request):
    return  templates.TemplateResponse("home.html",{"request": request, "title":"Home Page","Posts": Posts})

@app.get("/posts/{post_id}", name='Post')        # Get a single Post by ID
def get_posts(request:Request, post_id: int):
    for post in Posts:
        if post.get("id") == post_id:
            title = post['title'][:]
            return templates.TemplateResponse(request, "post.html",{"title":"Post Page","Post": post})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not Found")

@app.get("/api/posts")
def get_posts(request:Request):
    return Posts

@app.get("/api/posts/{post_id}")        # Get a single Post by ID
def get_posts(post_id: int):
    for post in Posts:
        if post.get("id") == post_id:
            return post
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not Found")