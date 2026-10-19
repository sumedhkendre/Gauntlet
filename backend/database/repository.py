import uuid

from database.database import get_connection


def create_session(description=""):
    session_id = str(uuid.uuid4())

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO sessions (id, description)
        VALUES (?, ?)
        """,
        (session_id, description)
    )

    connection.commit()
    connection.close()

    return session_id


def create_attack(session_id, prompt, attack_type, generated_by="attacker"):
    attack_id = str(uuid.uuid4())

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO attacks
        (id, session_id, prompt, attack_type, generated_by)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            attack_id,
            session_id,
            prompt,
            attack_type,
            generated_by
        )
    )

    connection.commit()
    connection.close()

    return attack_id


def save_target_response(
    attack_id,
    response,
    model_name
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO target_responses
        (attack_id, response, model_name)
        VALUES (?, ?, ?)
        """,
        (
            attack_id,
            response,
            model_name
        )
    )

    connection.commit()
    connection.close()


def save_evaluation(
    attack_id,
    rule_result,
    llm_result,
    similarity_result,
    final_result,
    confidence,
    reason
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO evaluations
        (
            attack_id,
            rule_result,
            llm_result,
            similarity_result,
            final_result,
            confidence,
            reason
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            attack_id,
            rule_result,
            llm_result,
            similarity_result,
            final_result,
            confidence,
            reason
        )
    )

    connection.commit()
    connection.close()


def save_memory_record(
    attack_id,
    root_cause,
    outcome,
    related_attack_id=None,
    confidence=0.0,
    stored_by="system"
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO memory_records
        (
            attack_id,
            root_cause,
            outcome,
            related_attack_id,
            confidence,
            stored_by
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            attack_id,
            root_cause,
            outcome,
            related_attack_id,
            confidence,
            stored_by
        )
    )

    connection.commit()
    connection.close()


def get_attack(attack_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM attacks
        WHERE id = ?
        """,
        (attack_id,)
    )

    result = cursor.fetchone()

    connection.close()

    return result


def get_session_attacks(session_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM attacks
        WHERE session_id = ?
        ORDER BY created_at
        """,
        (session_id,)
    )

    results = cursor.fetchall()

    connection.close()

    return results