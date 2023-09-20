from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(
        # id=uuid4(), 
        id=UUID("350568e7-e87a-467b-a3c8-805ce837d9dc"),
        first_name="Ana", 
        last_name="Maria", 
        email="email@gmail.com", 
        role=[Role.role_1]
    ),
    User(
        # id=uuid4(), 
        id=UUID("9d76ed2b-240e-4a65-9958-b651dd906738"),
        first_name="Gleici", 
        last_name="Silva", 
        email="email@gmail.com", 
        role=[Role.role_2]
    ),
    User(
        # id=uuid4(),
        id=UUID("54df3ed1-3e68-46cb-b4e0-65bebfc9a71e"), 
        first_name="Maísa", 
        last_name="Batista", 
        email="email@gmail.com", 
        role=[Role.role_3]
    ),
]

@app.get("/")
async def root():
    return {"message: Olá, WoMarks!"}

@app.get("/api/users")
async def get_users():
    return db;

#Busca dado
@app.get("/api/users/{id}")
async def get_users(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado!"}

#Criação de um nodo dado
@app.post("/api/users")
async def add_user(user: User):
    """
    Adicionado um usuário na base de dados:
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    """
    db.append(user)
    return {"id": user.id}


#Criação de uma função assíncrona de http put requests

#Atualização de Dados
@app.put("/api/users/{id}")
async def upgrade_user(id: UUID, user_upgrade: User):
    for user in db:
        if user.id == id:
            user.first_name = user_upgrade.first_name
            user.last_name = user_upgrade.last_name
            user.email = user_upgrade.email
            user.role = user_upgrade.role
            return {"Message": "Usuário atualizado com sucesso"}
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com id {id} não encontrado."
    )

#Remoção de Dados
@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o id {id} não encontrado!"
    )