from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from deps import get_db
import models

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])
templates = Jinja2Templates(directory="templates")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("/", response_class=HTMLResponse)
def listar_usuarios(request: Request, db: Session = Depends(get_db)):
    usuarios = db.query(models.User).all()
    return templates.TemplateResponse(
        "usuarios.html",
        {"request": request, "usuarios": usuarios}
    )


@router.get("/novo", response_class=HTMLResponse)
def novo_usuario(request: Request):
    return templates.TemplateResponse("novo_usuario.html", {"request": request})


@router.post("/novo")
def criar_usuario(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    username = username.strip()
    password = password.strip()

    if not username or not password:
        return templates.TemplateResponse(
            "novo_usuario.html",
            {"request": request, "error": "Preencha todos os campos"}
        )

    usuario_existente = db.query(models.User).filter(
        models.User.username == username
    ).first()

    if usuario_existente:
        return templates.TemplateResponse(
            "novo_usuario.html",
            {"request": request, "error": "Nome de usuário já existe"}
        )

    senha_hash = pwd_context.hash(password)

    novo = models.User(
        username=username,
        password=senha_hash
    )

    db.add(novo)
    db.commit()
    db.refresh(novo)

    return RedirectResponse("/usuarios/", status_code=303)