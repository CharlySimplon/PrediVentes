import uvicorn
from fastapi import FastAPI, APIRouter, Depends, HTTPException, Query

from sqldb import crud, models, schemas
from sqldb.database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session

from typing import Optional

app = FastAPI()
api_router = APIRouter()


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

@api_router.get("/categories/{id}")
def read_category_by_id(id: int, db : Session = Depends(get_db)):
    category = crud.get_category_by_id(db, id=id)
    if category is None :
        raise HTTPException(status_code=404, detail="Entity not found")
    return category

@api_router.get("/product/{id}")
def read_product_by_id(id: int, db : Session = Depends(get_db)):
    product = crud.get_product_by_id(db, id=id)
    if product is None :
        raise HTTPException(status_code=404, detail="Entity ID not found")
    return product

@api_router.get("/search/", status_code=200)
def search_recipes(
    *,
    keyword: Optional[str] = Query(None, min_length=3, example="chicken"),
    max_results: Optional[int] = 10,
    db: Session = Depends(get_db),
) -> dict:
    """
    Search for recipes based on label keyword
    """
    recipes = crud.recipe.get_multi(db=db, limit=max_results)
    if not keyword:
        return {"results": recipes}

    results = filter(lambda recipe: keyword.lower() in recipe.label.lower(), recipes)
    return {"results": list(results)[:max_results]}


app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("main:app")

# with open('dump.csv', 'wb') as f:
#     out = csv.writer(f)
#     out.writerow(['id', 'description'])

#     for item in session.query(Queue).all():
#         out.writerow([item.id, item.description])









