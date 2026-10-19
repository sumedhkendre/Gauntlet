from fastapi import APIRouter

from agents.strategist import generate_strategy

router = APIRouter(
    prefix="/api/strategist",
    tags=["Strategist"]
)


@router.get("/{session_id}")
def get_strategy(session_id: str):
    return generate_strategy(session_id)