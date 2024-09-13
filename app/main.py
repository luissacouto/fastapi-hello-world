from fastapi import FastAPI 
import os
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import sessionmaker

app = FastAPI(
    title="FastAPI - Hello World",
    description="This is the Hello World of FastAPI.",
    version="1.0.0",
) 


@app.get("/")
def hello_world():
    # engine = create_async_engine(DATABASE_URL, echo=True)
    # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    # return {"Hello": f"World: {beautiful}"}
    return {"Hello": f"World {DB_HOST}, {DB_USER}, {DB_PASSWORD}, {DB_NAME}"}