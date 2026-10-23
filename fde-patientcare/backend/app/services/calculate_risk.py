def calculate_risk(record):
    score = 0

    if record["number_inpatient"]!= None and record["number_inpatient"] >= 3:
        score += 3

    if record["number_emergency"]!= None and record["number_emergency"] >= 2:
        score += 2

    if record["number_outpatient"]!= None and record["number_outpatient"] >= 3:
        score += 1

    if record["time_in_hospital"]!= None and record["time_in_hospital"] >= 7:
        score += 1

    if record["num_medications"]!= None and record["num_medications"] >= 20:
        score += 1

    if score <= 2:
        risk_level = "LOW"
    elif score <= 4:
        risk_level = "MEDIUM"
    else:
        risk_level = "HIGH"

    return score, risk_level