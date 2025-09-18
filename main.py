from fastapi import FastAPI, APIRouter, HTTPException, Depends, status, Form
from models.User import user as User, RegisterUser
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from services.data import users_db
from passlib.context import CryptContext

app = FastAPI() 
router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    if not pwd_context.verify(form.password, user_db["password"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    return {"Inicio de sesión": form.username}

@router.post("/register")
async def register(id: int = Form(...), username: str = Form(...), password: str = Form(...)):
    if len(password) < 8 or len(password) > 12:
        raise HTTPException(status_code=400, detail="La contraseña debe tener entre 8 y 12 caracteres")
    if username in users_db:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    hashed_password = pwd_context.hash(password)
    users_db[username] = {"id": id, "username": username, "password": hashed_password}
    return {"msg": "Usuario registrado"}


@router.get("/user/{username}")
async def get_user(username: str):
    user = users_db.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user



app.include_router(router)