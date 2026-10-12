import json
from pathlib import Path

from fastapi import APIRouter
# Import the invoices list from the other file
router = APIRouter()  # router initialization
INVOICES_FILE = Path(__file__).with_name("invoices.json")

invoices = []
def load_invoices():
    try:
        with INVOICES_FILE.open("r") as file:
            invoices[:] = json.load(file)   # [start:end:step] - slicing - here it replaces entire items from start to end and replace with new items from json.load(file)     
    except FileNotFoundError:
        return {"error": "Invoices file not found."}


@router.get("/invoices")
def get_invoices(): 
    return invoices

@router.get("/invoices/{invoice_id}")
def get_invoice_by_id(invoice_id: int):
    for invoice in invoices:
        if invoice["id"] == invoice_id:
            return invoice
    return {"error": "Invoice not found"}

@router.post("/invoices")
def add_invoice(invoice: dict):

    invoices.append(invoice)
    with INVOICES_FILE.open("w") as file:
        json.dump(invoices, file, indent=4)
    return {"message": "Invoice added successfully", "invoice": invoice}



@router.delete("/invoices/{invoice_id}")
def delete_invoice(invoice_id: int):
    for invoice in invoices:
        if invoice["id"] == invoice_id:
            invoices.remove(invoice)
            with INVOICES_FILE.open("w") as file:
                json.dump(invoices, file, indent=4)
            return {"message": "Invoice deleted successfully"}
    return {"error": "Invoice not found"}

@router.put("/invoices/{invoice_id}")
def update_invoice(invoice_id: int, updated_invoice: dict):
    for index, invoice in enumerate(invoices):  # enumerate() returns both the index and the value of the item in the list
        if invoice["id"] == invoice_id:
            invoices[index] = updated_invoice # the index value points to the position of the invoice in the invoices dict, and we replace it with the updated_invoice
            with INVOICES_FILE.open("w") as file:
                json.dump(invoices, file, indent=4)
            return {"message": "Invoice updated successfully", "invoice": updated_invoice}
    return {"error": "Invoice not found"}

@router.patch("/invoices/{invoice_id}")
def patch_invoice(invoice_id: int, partial_invoice: dict): # method expects only a partical json object, not the entire invoice object
    for index, invoice in enumerate(invoices):
        if invoice["id"] == invoice_id:
            invoices[index].update(partial_invoice)  # update() method updates the existing dictionary with the new key-value pairs from partial_invoice
            with INVOICES_FILE.open("w") as file:
                json.dump(invoices, file, indent=4)
            return {"message": "Invoice patched successfully", "invoice": invoices[index]}
    return {"error": "Invoice not found"}