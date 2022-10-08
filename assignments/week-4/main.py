from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
import requests

#We generate a new FastAPI app in the Prod environment
#https://fastapi.tiangolo.com/

app = FastAPI(title='Service')

#Call your get function for a health Check
@app.get("/", tags=["Health Check"])
async def root():
    #requests.get()
    return {"message": "Ok"}
#to receive both (face-bokeh and face-emotion)
