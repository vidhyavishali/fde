
import json
from pathlib import Path
INVOICES_FILE = Path(__file__).parent / "data" / "invoices_mini.json"


with open(INVOICES_FILE, 'r') as file:
   invoices = json.load(file)

duplicates = []
for index,invoice in enumerate(invoices):
    if invoice in invoices[:index]:  #using slicing to check for duplicates up to the current index
        duplicates.append({index : invoice})

"""  # Triple quotes are for string literals that are ignored in runtime, but can be used for multi-line comments in code.
        #optional: remove duplicates from the list

seen = set()
duplicates=[]
for invoice in invoices:
    invoice_tuple = tuple(invoice.items())  # Convert the dictionary to a tuple of items for hashing
    if invoice_tuple in seen:
        duplicates.append(invoice)
    else:
        seen.add(invoice_tuple)  

"""


print("Duplicate invoices found:")
for duplicate in duplicates:
    for key, value in duplicate.items():
        print(f"  - {value} is in duplicates at the {key}")





#grouping invoices by vendor total amount
vendor_totals = {}
for invoice in invoices:
   vendor = invoice["vendor"]
   amount = float(invoice["amount"])
   vendor_totals[vendor] = vendor_totals.get(vendor, 0) + amount

print("Vendor total amounts:")
for vendor, total in vendor_totals.items():
   print(f"  - {vendor}: ${total:.2f}")
   