from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base # Importa as funções necessárias do SQLAlchemy para criar o mecanismo de banco de dados, a classe de sessão e a classe base para os modelos de banco de dados.

DATABASE_URL = "sqlite:///./pedidos.db" # A URL de conexão para o banco de dados SQLite. O arquivo do banco de dados será criado no diretório atual com o nome "pedidos.db".

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
) # Cria uma instância do mecanismo de banco de dados usando a URL de conexão. O argumento "connect_args" é necessário para permitir conexões simultâneas ao banco de dados SQLite.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Cria uma classe de sessão local usando a função sessionmaker do SQLAlchemy. Esta classe será usada para criar sessões de banco de dados para interagir com o banco de dados.

Base = declarative_base() # Cria uma classe base para os modelos de banco de dados usando a função declarative_base do SQLAlchemy. Os modelos de banco de dados serão definidos como subclasses desta classe base.