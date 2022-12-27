from fastapi import FastAPI
import uvicorn

app_p2 = FastAPI()

@app_p2.get("/")
def root():
    return {"data": "Сообщение от второго проекта"}

@app_p2.get("/data")
def data():
    return {"data": "Данные из второго проекта"}

if __name__ == "__main__":
    uvicorn.run("app:app_p2", host='0.0.0.0', port=80, reload=True)