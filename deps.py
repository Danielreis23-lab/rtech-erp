from database import SessionLocal # Importa a classe SessionLocal do módulo database. Esta classe é usada para criar sessões de banco de dados para interagir com o banco de dados.

def get_db():# Define a função get_db, é um gerador que fornece uma sessão de banco de dados para as rotas do FastAPI. Esta função é usada como uma dependência nas rotas para garantir que cada solicitação tenha acesso a uma sessão de banco de dados.
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()