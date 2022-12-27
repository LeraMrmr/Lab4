from fastapi import FastAPI
import requests
import os
import datetime
import uvicorn

app_p1 = FastAPI()

@app_p1.get(f"/")
def root():
    return {"data": "Сообщение от первого проекта"}

@app_p1.get(f"/data")
def data():
    url = os.environ.get('URL') + '/data'
    response = requests.get(url)
    return response.json()        

if __name__ == "__main__":
    uvicorn.run("app:app_p1", host='0.0.0.0', port=80, reload=True)