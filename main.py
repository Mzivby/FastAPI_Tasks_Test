from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    print("База готова к работе")
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


# запуск
if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=80, reload=True)