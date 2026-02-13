from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

@app.get("/")
async def home():
    html = Path("templates/index.html").read_text(encoding="utf-8")
    return HTMLResponse(html)
