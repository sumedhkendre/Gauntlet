from database.database import get_connection


def get_attack_relationships(attack_id: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            m.attack_id,
            m.root_cause,
            m.outcome,
            m.related_attack_id,
            m.confidence,
            m.stored_by,
            m.created_at
        FROM memory_records m
        WHERE m.attack_id = ?
           OR m.related_attack_id = ?
        ORDER BY m.created_at DESC
        """,
        (attack_id, attack_id)
    )

    results = cursor.fetchall()
    connection.close()

    return [dict(row) for row in results]


def get_session_graph(session_id: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            a.id AS attack_id,
            a.session_id,
            a.attack_type,
            a.prompt,
            e.final_result,
            e.confidence
        FROM attacks a
        LEFT JOIN evaluations e
            ON a.id = e.attack_id
        WHERE a.session_id = ?
        ORDER BY a.created_at
        """,
        (session_id,)
    )

    results = cursor.fetchall()
    connection.close()

    return [dict(row) for row in results]