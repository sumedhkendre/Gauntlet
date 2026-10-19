from graph_memory.memory_service import retrieve_memories


def generate_strategy(session_id: str):
    memories = retrieve_memories(limit=10)

    if not memories:
        return {
            "session_id": session_id,
            "strategy": "No previous attack memory available. Start with a basic security test.",
            "memory_count": 0
        }

    failed_attacks = [
        memory
        for memory in memories
        if str(memory.get("outcome", "")).upper() == "FAIL"
    ]

    if failed_attacks:
        strategy = (
            "Previous attacks show failed outcomes. "
            "Generate variations of previously observed attack patterns."
        )
    else:
        strategy = (
            "No previous failed attack pattern was found. "
            "Generate a diverse set of security test prompts."
        )

    return {
        "session_id": session_id,
        "strategy": strategy,
        "memory_count": len(memories)
    }