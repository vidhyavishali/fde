from fastapi import FastAPI
from models import Payment
import services as payService

app = FastAPI()

@app.get("/payments", response_model=list[Payment])
def get_all_payments():

    return payService.get_all_payments_service()

@app.get("/payments/{payment_id}", response_model=Payment)
def get_payment_by_id(payment_id: int):
    return payService.get_payment_by_id_service(payment_id)    

@app.post("/payments", response_model=Payment)
def add_payment(recipient: str, amount: float, status: str, transactionid: str):
    return payService.add_payment_service(recipient, amount, status, transactionid)

@app.delete("/payments/{payment_id}")
def delete_payment(payment_id: int):
    return payService.delete_payment_service(payment_id)

@app.put("/payments/{payment_id}")
def update_payment(payment_id: int, updated_payment: Payment):
    return payService.update_payment_service(payment_id, updated_payment)
   