import uvicorn
from fastapi import FastAPI, APIRouter, Request, Depends
# from sqlalchemy.orm import Session

from sqldb import crud, models, schemas
from sqldb.database import SessionLocal, engine, get_db

app = FastAPI()
api_router = APIRouter()


@api_router.get("/")
async def root():
    return {"message": "TEST 2 "}

# @api_router.get("/stores/")
# async def read_entities(db: Session = Depends(get_db)):
#     entities = crud.get_all_entities(db)
#     return entities

app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)







