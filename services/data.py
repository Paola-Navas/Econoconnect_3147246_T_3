from fastapi import APIRouter, HTTPException, Form
from models.User import User

router = APIRouter()
users_db = []

@router.post("/register")
def register(id: int = Form(...), username: str = Form(...), password: str = Form(...)):
    for u in users_db:
        if u.username == username:
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    user = User(id=id, username=username, password=password)
    users_db.append(user)
    return {"msg": "Usuario registrado"}

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    for u in users_db:
        if u.username == username:
            if u.password == password:
                return {"Inicio de sesión": u.username}
            raise HTTPException(status_code=400, detail="La contraseña no es correcta")
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@router.get("/user/{username}")
def get_user(username: str):
    for u in users_db:
        if u.username == username:
            return u
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
