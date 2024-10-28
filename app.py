from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from utils.prompts import create_sql_prompt_template
from utils.engine import chat

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Prompt(BaseModel):
    user_prompt: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def generate_sql_query(prompt: Prompt):
    return chat(create_sql_prompt_template(prompt.user_prompt))
