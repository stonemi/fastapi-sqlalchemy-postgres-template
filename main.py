import os
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
from config import Settings, loadSetting

def get_settings() -> Settings:
    return loadSetting()()

from security import validate_credentials

app = FastAPI(docs_url='/', dependencies=[Depends(validate_credentials)])

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from routes.posts import router as posts_router
from routes.basic import router as default_router

app.include_router(router=default_router, prefix="/basic",)
app.include_router(router=posts_router, prefix="/posts",)

if __name__ == '__main__' :
    uvicorn.run('main:app', host="127.0.0.1", port=8800, reload=True)




