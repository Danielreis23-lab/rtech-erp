# Rtech ERP

Sistema simples de ERP desenvolvido
com FastAPI, SQLAlchemy, Jinja2 e
SQLite para gerenciamento de pedidos,
produtos e controle de usuários.

## Funcionalidades
- Cadastro de usuário
- Login com autenticação via bcrypt
- Cadastro de produto
- Criação de pedidos
- Controle de status dos pedidos (Pendente, Em trânsito, Entregue, Cancelado)
- Painel com o valor pendente e faturado
- 2 gráficos para acompanhar o faturamento e venda por cliente

## Tecnologias
- FastAPI
- SQLAlchemy
- Jinja2
- SQLite
- Python
- HTML
- CSS
- JavaScript

## Estrutura do Projeto
```
projeto/
├── main.py
├── database.py
├── deps.py
├── models.py
├── popular_db.py
├── requirements.txt
├── .gitignore
├── README.md
├── pedidos.db
│
├── routers/
│   ├── __init__.py
│   ├── auth.py
│   ├── pedidos.py
│   └── usuarios.py
│
└── templates/
    ├── login.html
    ├── pedidos.html
    ├── usuarios.html
    └── novo_usuario.html
```

## Como rodar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. (Opcional) Popular o banco com dados de exemplo:
```bash
python popular_db.py
```

3. Inicie o servidor:
```bash
uvicorn main:app --reload
```

4. Acesse em: http://127.0.0.1:8000

## Período
Março de 2026

## Status
Em desenvolvimento