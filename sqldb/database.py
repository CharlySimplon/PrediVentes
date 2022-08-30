from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import os
# from dotenv import load_dotenv
# load_dotenv(override=True)

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123soleil@localhost:5432/leclerc_test"
# SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL").replace('postgres://','postgresql://')

DATABASE_URL_LECLERC="postgresql://WelleatAdminLeclerc:Gaudec42@leclerc-welleat.postgres.database.azure.com:5432/postgres"

engine = create_engine(DATABASE_URL_LECLERC)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()