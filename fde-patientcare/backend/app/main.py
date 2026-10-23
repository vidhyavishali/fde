from typing import Optional
from app.models.Encounter import Encounter, EncounterIn
from app.models.Intervention import Intervention
from app.models.CareQueue import CareQueue

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from app.services import patient_care_service as pc_service
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Shared by every list endpoint so a negative or huge limit is rejected with a 422.
LimitQuery = Query(default=10, ge=1, le=100, description="Number of records to return")

@app.get("/encounters", response_model=list[Encounter])
def get_encounters(limit: int = LimitQuery):
    return pc_service.get_all_encounters(limit)


@app.get("/patient/search", response_model=list[Encounter])
def search_encounters(
    patient_number: Optional[str] = None,
    risk_level: Optional[str] = None,
    risk_score: Optional[int] = None,
    limit: int = LimitQuery
):
    return pc_service.search_encounters(
        patient_number,
        risk_level.upper() if risk_level else None,
        risk_score,
        limit
    )

@app.get("/encounters/{encounter_id}", response_model=Encounter)
def get_encounter_by_id(encounter_id: int):
    encounter = pc_service.get_encounter_by_id(encounter_id)
    if encounter is None:
        raise HTTPException(status_code=404, detail="Encounter not found")
    return encounter

@app.get("/encounters/status/{status}", response_model=list[Encounter])
def get_encounters_by_status(status: str, limit: int = LimitQuery):
    return pc_service.get_encounters_by_status(status.upper(), limit)


@app.post("/encounters", response_model=Encounter, status_code=201)
def create_encounter(body: EncounterIn):
    return pc_service.save_encounter(body.patient_number, body.age, body.in_hospital_days, body.inpatient_visits, body.outpatient_visits, body.emergency_visits, body.medications)

@app.get("/care-queue", response_model=list[CareQueue])
def get_care_queue(limit: int = LimitQuery):
    return pc_service.get_care_queue(limit)     

@app.post("/interventions/{encounter_id}", response_model=Intervention)
def create_intervention(encounter_id: int, status: str, assigned_to: Optional[str] = None, notes: Optional[str] = None):
    intervention = pc_service.save_patient_care_intervention_by_encounter(encounter_id, status.upper(), assigned_to, notes)
    if intervention is None:
        raise HTTPException(status_code=404, detail="Encounter not found")
    return intervention


@app.get("/interventions/{encounter_id}", response_model=Intervention)
def get_intervention_by_encounter(encounter_id: int):
    intervention = pc_service.get_intervention_by_encounter(encounter_id)
    if intervention is None:
        raise HTTPException(status_code=404, detail="Intervention not found")
    return intervention

@app.get("/operational-summary") # optional does not show the default value in swagger like Query.
@app.get("/operational-summary/{status}")
def get_operational_summary(status: Optional[str] = None):
    return pc_service.get_operational_summary(status)


@app.get("/interventions", response_model=list[Intervention])
def get_all_interventions(limit: int = LimitQuery):
    return pc_service.get_all_interventions(limit)

@app.put("/interventions/{intervention_id}/update", response_model=Intervention)
def update_intervention(intervention_id: int, intervention: Intervention):
    intervention = pc_service.update_intervention(intervention_id, intervention.encounter_id, intervention.status.upper(), intervention.assigned_to, intervention.notes)
    if intervention is None:
        raise HTTPException(status_code=404, detail="Intervention or encounter not found")
    return intervention

