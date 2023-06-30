from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from app.api.api import api_router
from app.core.config import settings

import uvicorn

def initialize_backend_application() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        version=settings.VERSION,
        openapi_url=f"{settings.API_PREFIX}/{settings.OPENAPI_URL}"
    )

    app.add_middleware(
        CORSMiddleware,
        # allowed_origins=settings.ALLOWED_HOSTS or ["*"],
        allow_credentials=settings.IS_ALLOWED_CREDENTIALS,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )

    app.include_router(
        api_router,
        prefix=settings.API_PREFIX
    )
    
    return app


app: FastAPI = initialize_backend_application()


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        workers=settings.SERVER_WORKERS,
        log_level="debug",
        reload=settings.DEBUG,
    )