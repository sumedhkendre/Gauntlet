from database.repository import save_memory_record
from database.database import get_connection


def store_memory(
    attack_id: str,
    root_cause: str,
    outcome: str,
    related_attack_id: str | None = None,
    confidence: float = 0.0,
    stored_by: str = "system"
):
    save_memory_record(
        attack_id=attack_id,
        root_cause=root_cause,
        outcome=outcome,
        related_attack_id=related_attack_id,
        confidence=confidence,
        stored_by=stored_by
    )


def retrieve_memories(
    attack_id: str | None = None,
    limit: int = 10
):
    connection = get_connection()
    cursor = connection.cursor()

    if attack_id:
        cursor.execute(
            """
            SELECT *
            FROM memory_records
            WHERE attack_id = ?
               OR related_attack_id = ?
            ORDER BY created_at DESC
            LIMIT ?
            """,
            (attack_id, attack_id, limit)
        )
    else:
        cursor.execute(
            """
            SELECT *
            FROM memory_records
            ORDER BY created_at DESC
            LIMIT ?
            """,
            (limit,)
        )

    results = cursor.fetchall()
    connection.close()

    return [dict(row) for row in results]