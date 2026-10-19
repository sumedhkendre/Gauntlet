from agents.target import generate
from judge.heterogeneous_judge import evaluate
from database.repository import save_target_response, save_evaluation
from graph_memory.memory_service import store_memory
from config import TARGET_MODEL


def execute_attack(
    attack_id: str,
    prompt: str,
    session_id: str
):
    # 1. Send attack prompt to target LLM
    target_response = generate(prompt)

    # 2. Save target response
    save_target_response(
        attack_id=attack_id,
        response=target_response,
        model_name=TARGET_MODEL
    )

    # 3. Evaluate target response
    evaluation = evaluate(
        prompt=prompt,
        response=target_response
    )

    # 4. Save complete evaluation
    save_evaluation(
        attack_id=attack_id,
        rule_result=evaluation.rule_result.model_dump_json(),
        llm_result=evaluation.llm_result.model_dump_json(),
        similarity_result=(
            evaluation.similarity_result.model_dump_json()
            if evaluation.similarity_result
            else None
        ),
        final_result=evaluation.final_result,
        confidence=evaluation.confidence,
        reason=evaluation.reason
    )

    # 5. Store the result in graph memory
    store_memory(
        attack_id=attack_id,
        root_cause=evaluation.reason,
        outcome=evaluation.final_result,
        confidence=evaluation.confidence,
        stored_by="heterogeneous_judge"
    )

    return {
        "attack_id": attack_id,
        "session_id": session_id,
        "target_response": target_response,
        "evaluation": evaluation.model_dump()
    }