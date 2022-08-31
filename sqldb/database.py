from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import psycopg2
from dotenv import load_dotenv
load_dotenv(override=True)


# SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL").replace('postgres://','postgresql://')


# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123soleil@localhost:5432/leclerc_test"
SQLALCHEMY_DATABASE_URL = "postgresql://WelleatAdminLeclerc:Gaudec42@leclerc-welleat.postgres.database.azure.com:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()