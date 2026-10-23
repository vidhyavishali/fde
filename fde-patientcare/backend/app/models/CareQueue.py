from pydantic import BaseModel
from typing import Optional

class CareQueue(BaseModel):
    encounter_id: int
    patient_nbr: str
    age: str
    risk_score: float
    risk_level: str     
    status: Optional[str] = None
    assigned_to: Optional[str] = None
    notes: Optional[str] = None
    interventionId: Optional[int] = None