import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.site import version, title, description
from engine.api import health, completion

root_path = "/engine"
if os.getenv("ROUTE"):
    root_path = os.getenv("ROUTE")

app = FastAPI(
    title=title,
    version=version,
    description=description,
    docs_url="/v1/docs",
    openapi_url="/v1/openapi.json",
    root_path=root_path
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(completion.router)
# app.include_router(rag.router)


@app.get("/v1")
async def root():
    return {title: description}