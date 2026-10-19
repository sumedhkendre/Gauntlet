from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from database.database import initialize_database
from api.attack_routes import router as attack_router
from api.memory_routes import router as memory_router
from api.strategist_routes import router as strategist_router


app = FastAPI(title="GAUNTLET Backend")


# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": str(exc)
        }
    )


initialize_database()

app.include_router(attack_router)
app.include_router(memory_router)
app.include_router(strategist_router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "GAUNTLET backend is running"
    }