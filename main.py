from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import ast

app = FastAPI()

templates = Jinja2Templates(directory="templates/blog")

with open("snippets.txt", "r") as file:
    Posts = ast.literal_eval(file.read())

@app.get("/", response_class=HTMLResponse, include_in_schema=False)    # include_in_schema=False hides the route from the documentation
@app.get("/Posts", response_class=HTMLResponse)    # Multiple routes can navigate to same page
def home(request:Request):
    return  templates.TemplateResponse("home.html",{"request": request})

@app.get("/api/posts",response_class=HTMLResponse)
def get_posts(request:Request):
    return templates.TemplateResponse("home.html",{"Posts": Posts, "request": request})