from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# URL de conexão com o PostgreSQL do Docker (banco db_mobilidade_rj)
DATABASE_URL = "postgresql+psycopg://postgres:postgres@localhost:5433/db_mobilidade_rj"


engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



