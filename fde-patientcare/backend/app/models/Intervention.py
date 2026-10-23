from pydantic import BaseModel
from typing import Optional

class Intervention(BaseModel):
    intervention_id: Optional[int] = None
    encounter_id: int
    status: str
    assigned_to: Optional[str] = None
    notes: Optional[str] = None

