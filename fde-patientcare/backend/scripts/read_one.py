import csv
from scripts.clean_record import clean_record
from app.services.calculate_risk import calculate_risk
from pathlib import Path
from scripts.insert_record import insert_record

data_file = Path(__file__).resolve().parent.parent / "data" / "diabetic_data.csv"

with data_file.open("r") as file:
    reader = csv.DictReader(file)


    first_row = next(reader)

    print(first_row)
    
    clean_record_data = clean_record(first_row)
    score, risk_level = calculate_risk(clean_record_data)
    print("Clean Record:", clean_record_data)
    print("Risk Score:", score)
    print("Risk Level:", risk_level)
    insert_record(clean_record_data, score, risk_level)