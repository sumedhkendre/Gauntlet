from pydantic import BaseModel, Field
from schemas.result import EvaluationResult


class AttackRequest(BaseModel):
    session_id: str | None = None
    prompt: str = Field(..., min_length=1)
    attack_type: str = Field(..., min_length=1)


class AttackResponse(BaseModel):
    attack_id: str
    session_id: str
    target_response: str
    evaluation: EvaluationResult