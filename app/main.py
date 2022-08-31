from fastapi import FastAPI, APIRouter
import uvicorn


app = FastAPI(title="Welleat Data API", openapi_url="/openapi.json")

api_router = APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
    return {"msg": "Bienvenue sur l'API Data Welleat!"}


app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")






