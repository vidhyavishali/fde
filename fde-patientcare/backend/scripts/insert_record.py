from app.db.database import get_connection

def insert_record(record, score, risk_level):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO patient_encounters(
        encounter_id,
        patient_nbr,
        age,
        time_in_hospital,
        number_inpatient,
        number_emergency,
        number_outpatient,
        num_medications,
        readmitted,
        risk_score,
        risk_level
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """,
    (
        record["encounter_id"],
        record["patient_nbr"],
        record["age"],
        record["time_in_hospital"],
        record["number_inpatient"],
        record["number_emergency"],
        record["number_outpatient"],
        record["num_medications"],
        record["readmitted"],
        score,
        risk_level
    ))
    

    conn.commit()
    cursor.close()
    conn.close()