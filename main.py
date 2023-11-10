from fastapi import APIRouter, FastAPI

app = FastAPI()

health_router = APIRouter(prefix="/healthcheck", tags=["Health Check"])


@health_router.get("")
def check_service():
    return {"detail":"OK"}


app.include_router(health_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",port=8000)