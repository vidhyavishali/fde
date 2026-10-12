from pydantic import BaseModel


class Invoice(BaseModel):
    invoice_id: str
    vendor: str
    amount: float | None = None   # some rows have null
    status: str
    date: str                     # or datetime.date; "2026-09-03" parses fine
    deleted: bool = False         # file stores "false" as a string

class Payment(BaseModel):
    invoice_id: str
    paid: float