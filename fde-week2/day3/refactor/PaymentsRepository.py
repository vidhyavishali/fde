import json
from pathlib import Path

PAYMENTS_FILE = Path(__file__).parent.parent / "data" / "payments.json"


#the source is read only source, so we don't need to implement CRUD operations for payments. We just need to read the data and filter it based on invoice_id.

def load_payments():
    with open(PAYMENTS_FILE, 'r') as file:
      return json.load(file)


def get_payment_by_invoice_id(invoice_id):
    returnList = []
    payments = load_payments()
    for payment in payments:
        if payment["invoice_id"] == invoice_id:
            returnList.append(payment)
    return returnList
