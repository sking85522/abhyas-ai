from fastapi import FastAPI
from services.auth_service.api.routes import router
from shared.exceptions import setup_exception_handlers
from shared.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(title="Auth Service", version="1.0.0")

# Setup exception handlers from shared code
setup_exception_handlers(app)

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    logger.info("Auth Service started")

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "auth"}
