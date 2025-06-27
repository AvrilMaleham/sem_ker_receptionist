from fastapi import FastAPI
from utils import load_vectorstore, create_qa_chain
from contextlib import asynccontextmanager
from routes import router
import globals

@asynccontextmanager
async def lifespan(app: FastAPI):
    vectorstore = load_vectorstore()
    globals.qa_chain = create_qa_chain(vectorstore)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def test():
    return {"hello": "world"}

app.include_router(router, prefix="/chat", tags=["chat"])
