from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import ast

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'),name='static')

templates = Jinja2Templates(directory="templates/blog")

with open("snippets.txt", "r") as file:
    Posts = ast.literal_eval(file.read())

@app.get("/", include_in_schema=False, name='home')    # include_in_schema=False hides the route from the documentation
@app.get("/Posts", name='Posts')    # Multiple routes can navigate to same page
def home(request:Request):
    return  templates.TemplateResponse("home.html",{"request": request, "title":"Home Page","Posts": Posts})

@app.get("/api/posts")
def get_posts(request:Request):
    return Posts