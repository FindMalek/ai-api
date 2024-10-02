from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.site import version, title, description
from engine.routers import health, completion

app = FastAPI(
    title=title,
    version=version,
    description=description,
    docs_url="/v1/docs",
    openapi_url="/v1/openapi.json",
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


@app.get("/v1/helloFastApi")
def root():
    return {title: description}