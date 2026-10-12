from fastapi import FastAPI
from models import Invoice
from service import reconcile_invoices


app = FastAPI()


@app.get("/reconciled-invoices", response_model=list[Invoice])
def read_all_reconciled_invoices():
    return reconcile_invoices()