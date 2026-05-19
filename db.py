from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

DB_PASSWORD = quote_plus("asdf@9876")

DB_URL = f"mysql+pymysql://root:{DB_PASSWORD}@localhost:3306/updated_db_fastapi"


engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = True, bind = engine)

Base = declarative_base()