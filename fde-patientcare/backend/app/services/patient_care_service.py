
from app.repositories import patient_encounter_repository as encounterRepo
from app.repositories import care_intervention_repository as interventionRepo
from app.models.CareQueue import CareQueue
from app.services.calculate_risk import calculate_risk


def save_patient_care_intervention(encounter_id, status, assigned_to, notes):
    return interventionRepo.save_intervention(encounter_id, status, assigned_to, notes)


def save_patient_care_intervention_by_encounter(encounter_id, status, assigned_to, notes):
    if not get_encounter_by_id(encounter_id):
        return None
    return save_patient_care_intervention(encounter_id, status, assigned_to, notes) 

def get_all_encounters(limit):
    return encounterRepo.get_all_encounters(limit)

def get_encounter_by_id(encounter_id):
    return encounterRepo.get_encounter_by_id(encounter_id)

def get_care_queue(limit) -> list[CareQueue]:
    return [CareQueue(**row) for row in encounterRepo.get_care_queue(limit)]

def get_operational_summary(status):
    return encounterRepo.get_operational_summary(status)

def get_encounters_by_status(status, limit):
    return encounterRepo.get_encounters_by_status(status, limit)

def get_all_interventions(limit):
    return interventionRepo.get_all_interventions(limit)

def get_intervention_by_encounter(encounter_id):
    return  interventionRepo.get_intervention_by_encounter(encounter_id)

def update_intervention(intervention_id, encounter_id, status, assigned_to, notes):
    if not get_encounter_by_id(encounter_id):
        return None
    return interventionRepo.update_intervention(intervention_id, encounter_id, status, assigned_to, notes)

def save_encounter(patient_number, age, in_hospital_days, inpatient_visits, outpatient_visits, emergency_visits, medications):
    record = {"time_in_hospital": in_hospital_days or 0,
              "number_inpatient": inpatient_visits or 0,
              "number_emergency": emergency_visits or 0,
              "num_medications": medications or 0,
              "number_outpatient": outpatient_visits or 0}
    score, risk_level = calculate_risk(record)
    return encounterRepo.save_encounter(patient_number, age, record["time_in_hospital"], record["number_inpatient"],
                                        record["number_outpatient"], record["number_emergency"],
                                        record["num_medications"], score, risk_level)

def search_encounters(patient_number, risk_level, risk_score, limit):
    return encounterRepo.search_encounters(patient_number, risk_level, risk_score, limit)
