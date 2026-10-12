# It has basic CRUD Operations directly accessing the data source. 

import json
from pathlib import Path

INVOICES_FILE = Path(__file__).parent.parent / "data" / "invoices.json"



def get_all():  #get all invoices from the data source
    with open(INVOICES_FILE, 'r') as file:
        invoices = json.load(file)
    return [invoice for invoice in invoices ]


def save_invoices(invoices): # save the invoices back to the data source
      with open(INVOICES_FILE, 'w') as file:
         json.dump(invoices, file, indent=4) 



def add_invoice(invoice): #create a new invoice and save it to the data source
    invoices = get_all()
    invoices.append(invoice)
    save_invoices(invoices)


def find_invoice_by_id(invoice_id): #read an invoice by its ID
   invoices = get_all()
   for invoice in invoices:
      if invoice["invoice_id"] == invoice_id:
         return invoice 

def update_by_id(invoice_id, updated_invoice): #update an existing invoice by its ID
      invoices = get_all()
      for index, invoice in enumerate(invoices):
         if invoice["invoice_id"] == invoice_id:
               invoices[index] = updated_invoice
               save_invoices(invoices)
               return invoices[index]
  
   

def delete_by_id(invoice_id): #delete an invoice by its ID (soft delete by marking it as deleted)
    invoices = get_all()
    for index, invoice in enumerate(invoices):
        if invoice["invoice_id"] == invoice_id:
            invoice["deleted"] = True  # Mark the invoice as deleted
            save_invoices(invoices)
            return True
    return False
