

"""Clean a single row from the diabetic_data.csv file."""
def clean_record(row):
    return {
        "encounter_id": int(row["encounter_id"]),
        "patient_nbr": row["patient_nbr"],
        "age": row["age"],
        "time_in_hospital": int(row["time_in_hospital"]),
        "number_inpatient": int(row["number_inpatient"]),
        "number_emergency": int(row["number_emergency"]),
        "number_outpatient": int(row["number_outpatient"]),
        "num_medications": int(row["num_medications"]),
        "readmitted": row["readmitted"]
    }

print(type(clean_record({"encounter_id": "1", "patient_nbr": "1", "age": "50", "time_in_hospital": "5", "number_inpatient": "2", "number_emergency": "1", "number_outpatient": "3", "num_medications": "10", "readmitted": "NO"})["time_in_hospital"]))