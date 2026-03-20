from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from database import engine, Base
import models
from routers import auth
from routers import pedidos
from routers import usuarios

app = FastAPI()

# Criar tabelas
Base.metadata.create_all(bind=engine)

# Página inicial
@app.get("/")
def home():
    return RedirectResponse("/login", status_code=303)

# Rotas
app.include_router(auth.router)
app.include_router(pedidos.router)
app.include_router(usuarios.router)