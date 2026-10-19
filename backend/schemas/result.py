from pydantic import BaseModel, Field


class JudgeVerdict(BaseModel):
    passed: bool
    score: float = Field(..., ge=0.0, le=1.0)
    reason: str


class EvaluationResult(BaseModel):
    rule_result: JudgeVerdict
    llm_result: JudgeVerdict
    similarity_result: JudgeVerdict | None
    final_result: str
    confidence: float = Field(..., ge=0.0, le=1.0)
    reason: str