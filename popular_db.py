from sqlalchemy.orm import Session
from database import SessionLocal
from models import Produto, Pedido

db: Session = SessionLocal()

# PRODUTOS 
produtos = [
    Produto(nome="Notebook Dell", estoque=10, valor=3500),
    Produto(nome="Mouse Gamer", estoque=50, valor=120),
    Produto(nome="Teclado Mecânico", estoque=30, valor=280),
]

# PEDIDOS
pedidos = [
    Pedido(cliente="Carlos", produto="Notebook Dell", quantidade=1, total=3500, status="Entregue"),
    Pedido(cliente="Ana", produto="Mouse Gamer", quantidade=2, total=240, status="Pendente"),
]

db.add_all(produtos + pedidos)
db.commit()
db.close()

print("Banco populado com sucesso")