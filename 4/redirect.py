import requests
import json



from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
idx = "static/index.html"
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/redirect", response_class=HTMLResponse)
async def read_items():
    file_like = open(idx, mode="r")
    return "\n".join(file_like.readlines())