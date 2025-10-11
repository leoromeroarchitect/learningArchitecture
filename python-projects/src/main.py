from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Hola, Leonardo! 🚀 Tu primera API en FastAPI está corriendo."}