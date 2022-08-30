import uvicorn
from fastapi import FastAPI, APIRouter, Request
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

# from sqldb import crud, models, schemas
# from sqldb.database import SessionLocal, engine

app = FastAPI()
# app.add_middleware(HTTPSRedirectMiddleware)
api_router = APIRouter()


@api_router.get("/")
async def root():
    return {"message": "TEST 2 "}

app.include_router(api_router)

# @app.get("/{store}/all/{start}/{end}", response_model=schemas.??)
# async def get_all_predictions(store: str, start: int, end: int):
#     return

if __name__ == "__main__":
    uvicorn.run("main:app")







