from fastapi import FastAPI
from core.database import Base, engine
from api.v1.auth import router as auth_router

app = FastAPI(title="ProdFlow")

# Create tables
Base.metadata.create_all(bind=engine)

# Routes
app.include_router(auth_router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status": "OK", "message": "Backend LIVE"}