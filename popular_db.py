from sqlalchemy.orm import Session
from database import SessionLocal
from models import Produto, Pedido, User
from datetime import datetime
from passlib.context import CryptContext

db: Session = SessionLocal()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
 
 
usuario_admin = User(
    username="admin12",
    password=pwd_context.hash("741963"),
    role="admin"
)


produtos = [
    # Tênis
    Produto(nome="Tênis Nike Air Max 90",        estoque=25, valor=699.90),
    Produto(nome="Tênis Adidas Ultraboost 22",   estoque=18, valor=849.90),
    Produto(nome="Tênis Puma RS-X",              estoque=20, valor=499.90),
    Produto(nome="Tênis Vans Old Skool",         estoque=35, valor=379.90),
    Produto(nome="Tênis New Balance 574",        estoque=22, valor=549.90),
    Produto(nome="Tênis Converse Chuck Taylor",  estoque=40, valor=299.90),

    # Camisetas & Blusas
    Produto(nome="Camiseta Básica Branca P",     estoque=60, valor=59.90),
    Produto(nome="Camiseta Básica Preta M",      estoque=55, valor=59.90),
    Produto(nome="Camiseta Oversized G",         estoque=30, valor=89.90),
    Produto(nome="Blusa Cropped Feminina M",     estoque=40, valor=79.90),
    Produto(nome="Regata Dry-Fit Unissex G",     estoque=45, valor=49.90),

    # Calças & Shorts
    Produto(nome="Calça Jeans Skinny 38",        estoque=20, valor=189.90),
    Produto(nome="Calça Jeans Reta 40",          estoque=18, valor=179.90),
    Produto(nome="Calça Moletom Cinza M",        estoque=35, valor=129.90),
    Produto(nome="Short Tactel Masculino M",     estoque=50, valor=79.90),
    Produto(nome="Short Jeans Feminino 36",      estoque=28, valor=99.90),

    # Jaquetas & Moletons
    Produto(nome="Jaqueta Corta-Vento Nike M",   estoque=15, valor=349.90),
    Produto(nome="Moletom Canguru Preto G",      estoque=25, valor=199.90),
    Produto(nome="Jaqueta Jeans Feminina P",     estoque=12, valor=259.90),

    # Acessórios
    Produto(nome="Boné Aba Curva Preto",         estoque=70, valor=59.90),
    Produto(nome="Meia Cano Alto (Kit 3 pares)", estoque=100, valor=39.90),
    Produto(nome="Cinto Couro Marrom",           estoque=30, valor=69.90),
]


pedidos = [
    
    Pedido(cliente="Bruno Lima",       produto="Camiseta Básica Preta M",       quantidade=3, total=179.70,  status="Entregue", data_criacao=datetime(2026, 1, 8)),
    Pedido(cliente="Camila Torres",    produto="Jaqueta Jeans Feminina P",      quantidade=1, total=259.90,  status="Entregue", data_criacao=datetime(2026, 2, 14)),
    Pedido(cliente="Diego Alves",      produto="Tênis Adidas Ultraboost 22",    quantidade=1, total=849.90,  status="Entregue", data_criacao=datetime(2026, 2, 27)),
    Pedido(cliente="Patrícia Nunes",   produto="Short Jeans Feminino 36",       quantidade=2, total=199.80,  status="Entregue", data_criacao=datetime(2026, 3, 10)),
    Pedido(cliente="Thiago Martins",   produto="Meia Cano Alto (Kit 3 pares)",  quantidade=2, total=79.80,   status="Entregue", data_criacao=datetime(2026, 3, 22)),
    Pedido(cliente="Aline Ferreira",   produto="Moletom Canguru Preto G",       quantidade=1, total=199.90,  status="Entregue", data_criacao=datetime(2026, 4, 1)),

    # Pedidos pendentes
    Pedido(cliente="Marcos Rocha",     produto="Tênis New Balance 574",         quantidade=1, total=549.90,  status="Pendente"),
    Pedido(cliente="Sabrina Castro",   produto="Calça Jeans Skinny 38",         quantidade=1, total=189.90,  status="Pendente"),
    Pedido(cliente="Felipe Dias",      produto="Jaqueta Corta-Vento Nike M",    quantidade=1, total=349.90,  status="Pendente"),
    Pedido(cliente="Larissa Pinto",    produto="Camiseta Oversized G",          quantidade=2, total=179.80,  status="Pendente"),
    Pedido(cliente="Vinícius Gomes",   produto="Tênis Puma RS-X",               quantidade=1, total=499.90,  status="Pendente"),

    # Pedidos em trânsito
    Pedido(cliente="Isabela Ribeiro",  produto="Tênis Converse Chuck Taylor",   quantidade=1, total=299.90,  status="Em trânsito"),
    Pedido(cliente="Gustavo Cardoso",  produto="Short Tactel Masculino M",      quantidade=3, total=239.70,  status="Em trânsito"),
    Pedido(cliente="Natália Silva",    produto="Boné Aba Curva Preto",          quantidade=2, total=119.80,  status="Em trânsito"),

    # Pedidos cancelados
    Pedido(cliente="Rodrigo Fonseca",  produto="Cinto Couro Marrom",            quantidade=1, total=69.90,   status="Cancelado"),
    Pedido(cliente="Amanda Xavier",    produto="Regata Dry-Fit Unissex G",      quantidade=2, total=99.80,   status="Cancelado"),
]

db.add_all(produtos + pedidos)
db.commit()
db.close()

print(f"✅ Banco populado com sucesso!")
print(f"   • {len(produtos)} produtos cadastrados")
print(f"   • {len(pedidos)} pedidos registrados")