import csv
from scripts.clean_record import clean_record
from app.services.calculate_risk import calculate_risk
from pathlib import Path
from scripts.insert_record import insert_record

data_file = Path(__file__).resolve().parent.parent / "data" / "diabetic_data.csv"

with data_file.open("r") as file:
    reader = csv.DictReader(file)
    counter = 0
    next(reader) # skip column headers
    for row in reader:

        clean_record_data = clean_record(row)
        score, level = calculate_risk(clean_record_data)
        insert_record(clean_record_data, score, level)
        counter += 1

    print("Number of Records Imported:", counter)