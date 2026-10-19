from fastapi import APIRouter, HTTPException

from graph_memory.memory_service import retrieve_memories
from graph_memory.graph_memory import (
    get_attack_relationships,
    get_session_graph
)

router = APIRouter(
    prefix="/api/memory",
    tags=["Memory"]
)


@router.get("/attack/{attack_id}")
def attack_memory(attack_id: str):
    memories = retrieve_memories(
        attack_id=attack_id
    )

    return {
        "attack_id": attack_id,
        "memories": memories
    }


@router.get("/relationships/{attack_id}")
def attack_relationships(attack_id: str):
    relationships = get_attack_relationships(
        attack_id
    )

    return {
        "attack_id": attack_id,
        "relationships": relationships
    }


@router.get("/session/{session_id}")
def session_memory(session_id: str):
    graph = get_session_graph(
        session_id
    )

    if not graph:
        raise HTTPException(
            status_code=404,
            detail="No attacks found for this session."
        )

    return {
        "session_id": session_id,
        "attacks": graph
    }