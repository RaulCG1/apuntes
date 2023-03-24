
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"ID": "Hello World"}

@app.get("/")
async def root():
    return 2+2

@app.get("/url")
async def url():
    return {"ID":1234567,
            "nambe": "Raul"}

#Peticiones para https (get leer datos  post crear datos put actualizar datos  delete borrar datos) crud    