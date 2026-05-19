from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
import os 
from dotenv import load_dotenv

load_dotenv() 
DB_PASSWORD = os.getenv("DB_PASSWORD")

password = quote_plus(DB_PASSWORD)

DB_URL = f"mysql+pymysql://root:{password}@localhost:3306/updated_db_fastapi"


engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = True, bind = engine)

Base = declarative_base()