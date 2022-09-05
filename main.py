import uvicorn
from fastapi import FastAPI, APIRouter, Depends, HTTPException

from sqldb import crud, models, schemas
from sqldb.database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
import csv

import fcntl
# import msvcrt
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def testcron():
    with open("./tmp/test.txt", "w") as file:
        file.write("Message écrit à: %s' % datetime.now()")


    

app = FastAPI()
api_router = APIRouter()


@api_router.on_event('startup')
def scheduler_test():

    try:
        _ = open("./tmp/test.lock","w")
        _fd = _.fileno()
        # Pour Windows :
        # msvcrt.locking(_fd,msvcrt.LK_LOCK|msvcrt.LK_NBLCK,0)
        #Pour Linux :
        fcntl.lockf(_fd,fcntl.LOCK_EX|fcntl.LOCK_NB)


        scheduler = AsyncIOScheduler()
        scheduler.add_job(testcron, 'cron', minute="00,05,10,15,20,25,30,38,40,45,50,55")#minute= "*/1")#second='*/5')
        # scheduler.add_job(func.process_data_test, 'cron', second='*/5')
        scheduler.print_jobs()
        scheduler.start()

    except BlockingIOError:
        pass



@api_router.get("/")
async def root():
    return {"message": "TEST 4 "}

@api_router.get("/stores/")
async def read_entities(db: Session = Depends(get_db)):
    entities = crud.get_all_entities(db)
    return entities

@api_router.get("/categories/")
async def read_categories(db: Session = Depends(get_db)):
    categories = crud.get_all_categories(db)
    return categories

@api_router.get("/products/")
async def read_products(db: Session = Depends(get_db)):
    products = crud.get_all_products(db)
    return products


@api_router.get("/categories/{id}")
def read_category_by_id(id: int, db : Session = Depends(get_db)):
    category = crud.get_category_by_id(db, id=id)
    if category is None :
        raise HTTPException(status_code=404, detail="Entity not found")
    return category

@api_router.get("/products/{id}")
def read_product_by_id(id: int, db : Session = Depends(get_db)):
    product = crud.get_product_by_id(db, id=id)
    if product is None :
        raise HTTPException(status_code=404, detail="Entity ID not found")
    return product



app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("main:app")

# with open('dump.csv', 'wb') as f:
#     out = csv.writer(f)
#     out.writerow(['id', 'description'])

#     for item in session.query(Queue).all():
#         out.writerow([item.id, item.description])










