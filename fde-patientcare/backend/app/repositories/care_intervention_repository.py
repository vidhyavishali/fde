from app.db.database import get_connection

def get_all_interventions(limit):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM care_interventions LIMIT %s", (limit,))
    interventions = cursor.fetchall()
    cursor.close()
    connection.close()
    return interventions

def get_intervention_by_encounter(encounter_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM care_interventions WHERE encounter_id = %s", (encounter_id,))
    interventions = cursor.fetchone()
    cursor.close()
    connection.close()
    return interventions

def save_intervention(encounter_id, status, assigned_to, notes):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO care_interventions (encounter_id, status, assigned_to, notes) VALUES (%s, %s, %s, %s) "
        "ON CONFLICT (encounter_id) DO UPDATE SET status = EXCLUDED.status, assigned_to = EXCLUDED.assigned_to, notes = EXCLUDED.notes "
        "RETURNING *",
        (encounter_id, status, assigned_to, notes)
    )
    intervention = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    return intervention

def update_intervention(intervention_id, encounter_id, status, assigned_to, notes):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE care_interventions SET encounter_id = %s, status = %s, assigned_to = %s, notes = %s WHERE intervention_id = %s RETURNING *",
        (encounter_id, status, assigned_to, notes, intervention_id)
    )
    intervention = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    return intervention