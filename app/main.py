from fastapi import FastAPI

from app.api.v1.tickets import router as tickets_router

app = FastAPI(
    title="IT Service Desk API",
    description="Backend API for the IT Service Desk AI Agent",
    version="1.0.0",
)

app.include_router(
    tickets_router,
    prefix="/api/v1/tickets",
    tags=["Tickets"],
)


@app.get("/health", tags=["System"])
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "IT Service Desk API",
    }