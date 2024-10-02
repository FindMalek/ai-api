from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.site import version, title, description
from app.routers import health, completion

app = FastAPI(
    title=title,
    version=version,
    description=description,
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(health.router)
app.include_router(completion.router)
# app.include_router(rag.router)


@app.get("/api/helloFastApi")
def root():
    return {title: description}