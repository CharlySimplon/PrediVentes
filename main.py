import uvicorn
from fastapi import FastAPI, APIRouter

# from sqldb import crud, models, schemas
# from sqldb.database import SessionLocal, engine, get_db

app = FastAPI()
api_router = APIRouter()


@api_router.get("/")
async def root():
    return {"message": "TEST 2 "}

app.include_router(api_router)

# @api_router.get("/stores/")
# async def read_entities(db: Session = Depends(get_db)):
#     entities = crud.get_all_entities(db)
#     return entities




if __name__ == "__main__":
    uvicorn.run("main:app")







