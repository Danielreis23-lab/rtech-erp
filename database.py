
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base # Importa as funções necessárias do SQLAlchemy para criar o mecanismo de banco de dados.

DATABASE_URL = "sqlite:///./pedidos.db" 

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

Base = declarative_base() 