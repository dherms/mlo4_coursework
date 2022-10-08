from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
import requests

#We generate a new FastAPI app in the Prod environment
#https://fastapi.tiangolo.com/

app = FastAPI(title='Service')

#Call your get function for a health Check
@app.get("/", tags=["Health Check"])
async def root():
    bokeh_response = requests.get("http://face-bokeh:8000/")
    emotion_response = requests.get("http://face-emotion:8000/")
    response = {
        "face-bokeh": bokeh_response.json()["message"],
        "face-emotion": emotion_response.json()["message"]
    }
    return response
