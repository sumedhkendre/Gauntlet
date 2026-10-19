from fastapi import Depends
from api.auth import verify_api_key
from fastapi import APIRouter
from schemas.attack import AttackRequest, AttackResponse
from database.repository import create_session, create_attack
from services.attack_service import execute_attack

router = APIRouter(
    prefix="/api/attacks",
    tags=["Attacks"],
    dependencies=[Depends(verify_api_key)]
)


@router.post("/")
def create_attack_endpoint(request: AttackRequest):

    session_id = request.session_id

    if session_id is None:
        session_id = create_session(
            description="GAUNTLET attack session"
        )

    attack_id = create_attack(
        session_id=session_id,
        prompt=request.prompt,
        attack_type=request.attack_type,
        generated_by="attacker"
    )

    result = execute_attack(
        attack_id=attack_id,
        prompt=request.prompt,
        session_id=session_id
    )

    return result