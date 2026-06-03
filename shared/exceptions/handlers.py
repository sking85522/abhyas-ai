from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .custom_exceptions import AppError
from shared.logger import get_logger

logger = get_logger(__name__)

def setup_exception_handlers(app: FastAPI):
    @app.exception_handler(AppError)
    async def app_error_handler(request: Request, exc: AppError):
        logger.error(f"AppError: {exc.message} on {request.url}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": True, "message": exc.message}
        )

    @app.exception_handler(Exception)
    async def global_error_handler(request: Request, exc: Exception):
        logger.exception(f"Unhandled Exception on {request.url}: {exc}")
        return JSONResponse(
            status_code=500,
            content={"error": True, "message": "Internal Server Error"}
        )
