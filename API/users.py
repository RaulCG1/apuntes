from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
#uvicorn users:app --reload

class Usuarios(BaseModel):
    id: int
    name: str
    surname:str
    url : str
    age: int

users_list = [Usuarios(id=1,name="Raul",surname="Calderon",url="google.com",age=23),
         Usuarios(id=2,name="Alfonso",surname="Calderon",url="afs.com",age=60),
         Usuarios(id=3,name="Paco",surname="Calderon",url="pa.com",age=30)
         ]

""" Echo a mano mas tardado
@app.get("/usersjson")
async def usersjson():
    return [{"name": "Raul","surname":"Calderon","url": "google.com","age":23},
       {"name": "Alfonso","surname":"Calderon","url": "afs.com","age":23},]
"""
@app.get("/usuarios") #usando modelo basemodel
async def users_lista():
    return users_list

#path

@app.get("/usuario/{id},{name}") #usando modelo basemodel
async def user(id: int, name:str):
    return buscar_usuario(id,name)
    
#query
@app.get("/usuario/") #usando modelo basemodel
async def user(id: int,name :str):
    return buscar_usuario(id,name)
    

@app.post("/usuario/")
async def user_add(user : Usuarios):
    if buscar_usuario(user.id,user.name) in users_list:
        return {"error":"Usuario repetido "}
    else:
        users_list.append(user)
        return user

@app.put("/usuario/")
async def user_act(user : Usuarios):
    found = False

    for index, usuario in enumerate(users_list):
        if usuario.id == user.id:
            users_list[index] = user
            found=True
    if not found:
        return {"error":"No se encontro el usuario"}
    else:
        return user


@app.delete("/usuario/{id}")
async def delete_user(id: int):
    found = False
    for index, usuario in enumerate(users_list):
        if usuario.id == id:
            del users_list[index]
            found=True
    if not found:
        return {"error":"No se encontro el usuario para eliminar"}
    else:
        return user

def buscar_usuario(id: int, name :str):
    usuarios=filter(lambda user : user.id ==id and user.name == name,users_list)
    try:
        return list(usuarios)[0]
    except:
        return {"error":"Usuario no encontrado"}
    
#POST PUT DELETE

