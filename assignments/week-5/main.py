from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
import requests

# Let's generate a new FastAPI app
# Generate a FastAPI instance called `app` with the title 'Triton Health Check'
# https://fastapi.tiangolo.com/


#Call your get function for a health Check
#to receive both (face-bokeh and face-emotion)
app = FastAPI(title="Triton Health Check")

@app.get("/", tags=["Health Check"])
async def root():
  bokeh_response = requests.get("http://face-bokeh:8000/")
  emotion_response = requests.get("http://face-emotion:8000/")
  triton_response_code = requests.get("http://triton:8000/v2/health/ready").status_code
  if triton_response_code == 200:
      triton_response = "Ok"
  else:
      trition_response = "Error"
  response = {
      "face-bokeh": bokeh_response.json()["message"],
      "face-emotion": emotion_response.json()["message"],
      "triton": triton_response
  }
  return response
