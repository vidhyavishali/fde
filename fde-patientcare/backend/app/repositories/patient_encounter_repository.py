from app.db.database import get_connection

def get_all_encounters(limit):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM patient_encounters order by encounter_id desc LIMIT %s", (limit,))
    encounters = cursor.fetchall()
    cursor.close()
    connection.close()
    return encounters

def get_encounter_by_id(encounter_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM patient_encounters WHERE encounter_id = %s", (encounter_id,))
    encounter = cursor.fetchone()
    cursor.close()
    connection.close()
    return encounter

def get_care_queue(limit):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT e.encounter_id, e.patient_nbr, e.age, e.risk_score, e.risk_level,
               i.intervention_id AS "interventionId", i.status, i.assigned_to, i.notes
        FROM patient_encounters e
        LEFT JOIN care_interventions i ON i.encounter_id = e.encounter_id
        WHERE e.risk_level IN ('MEDIUM', 'HIGH')
        LIMIT %s
    """, (limit,))
    care_queue = cursor.fetchall()
    cursor.close()
    connection.close()
    return care_queue

def get_operational_summary(status):
    connection = get_connection()
    cursor = connection.cursor()
    query_str = "SELECT"
    status = status.upper() if status else None
    if (status is None or status not in ['LOW', 'MEDIUM', 'HIGH']):
        query_str +=    " COUNT(*) AS total_encounters"
    else:
        query_str += " SUM(CASE WHEN risk_level = %s THEN 1 ELSE 0 END) AS " + "count"

# ( status, ) represents a tuple containing the status value for the SQL query parameterization. 
# This tuple replaces %s in the SQL query.   
    query_str += " FROM patient_encounters"
    cursor.execute(query_str, (status,) if status in ['LOW', 'MEDIUM', 'HIGH'] else ())
    summary = cursor.fetchone()
    cursor.close()
    connection.close()
    return summary

def get_encounters_by_status(status, limit):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM patient_encounters WHERE risk_level = %s LIMIT %s", (status.upper(), limit))
    encounters = cursor.fetchall()
    cursor.close()
    connection.close()
    return encounters


def save_encounter(patient_number, age, in_hospital_days, inpatient_visits, outpatient_visits, emergency_visits, medications, risk_score, risk_level):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO patient_encounters (patient_nbr, age, time_in_hospital, number_inpatient, number_outpatient, number_emergency, num_medications, risk_score, risk_level)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING *
    """, (patient_number, age, in_hospital_days, inpatient_visits, outpatient_visits, emergency_visits, medications, risk_score, risk_level))
    row = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    return row


def search_encounters(patient_number, risk_level, risk_score, limit):
    connection = get_connection()
    cursor = connection.cursor()

    exec_query = "SELECT * FROM patient_encounters where 1=1"
    params = []
    if patient_number:
        exec_query += " AND patient_nbr = %s"
        params.append(patient_number)
    if risk_level:
        exec_query += " AND risk_level = %s"
        params.append(risk_level)
    if risk_score is not None:
        exec_query += " AND risk_score = %s"
        params.append(risk_score)
    exec_query += " LIMIT %s"
    params.append(limit)

    cursor.execute(exec_query, tuple(params))
    encounters = cursor.fetchall()
    cursor.close()
    connection.close()
    return encounters