from pydantic import BaseModel

class Payment(BaseModel):
    id: int
    recipient: str
    amount: float
    status: str
    transactionid: str