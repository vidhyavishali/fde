from pydantic import BaseModel
from typing import Optional


class EncounterIn(BaseModel):
    patient_number: str
    age: str
    in_hospital_days: Optional[int] = None
    inpatient_visits: Optional[int] = None
    outpatient_visits: Optional[int] = None
    emergency_visits: Optional[int] = None
    medications: Optional[int] = None


class Encounter(BaseModel):
    encounter_id: int
    patient_nbr: str
    age: str
    time_in_hospital: int
    number_inpatient: int
    number_emergency: int
    number_outpatient: int
    num_medications: int
    readmitted: Optional[str] = None
    risk_score: int
    risk_level: str