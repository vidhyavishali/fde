import json
from models import Invoice
import PaymentsRepository as paymentRepo
import InvoiceRepository as invoiceRepo


def clean_invoices(invoices) -> list[dict]:
    print(f'Cleaning from {len(invoices)} invoices')
    if invoices is None:
        return []

    duplicates = []
    active_invoice_list = remove_deleted_invoices(invoices)
    normalised_vendor_invoice_list = normaliseInvoiceDetails(active_invoice_list)
    actual_invoice_list = remove_duplicatesByRule(normalised_vendor_invoice_list, duplicates)
    true_invoice_list = remove_suspected_duplicates(actual_invoice_list)
    return true_invoice_list


# The invoice is not actually deleted; a deleted flag is used instead.
# The flag may be stored as a bool or as the string "true"/"false".
def is_deleted(invoice) -> bool:
    deleted = invoice.get("deleted", False)
    if isinstance(deleted, str):
        return deleted.strip().lower() == "true"
    return bool(deleted)


def remove_deleted_invoices(invoices) -> list[dict]:
    print(f'Removing deleted invoices from {len(invoices)} invoices')
    if invoices is None:
        return []
    return [invoice for invoice in invoices if not is_deleted(invoice)]


# Vendor names differ only by case or trailing spaces. They are the same vendor.
# Normalize. Clean the vendor (strip, title-case) and the status (upper-case).
# Do it in place using the index. Report rows where the amount is invalid and exclude them.
def normaliseInvoiceDetails(invoices) -> list[dict]:
    print(f'Normalising {len(invoices)} invoices')
    if invoices is None:
        return []

    valid_invoices = []
    for index, invoice in enumerate(invoices):
        invoice["vendor"] = invoice["vendor"].strip().title()
        invoice["status"] = invoice.get("status", "PENDING").upper()

        try:
            invoice["amount"] = float(invoice["amount"])
        except (TypeError, ValueError):
            print(f'Row {index} ({invoice.get("invoice_id", "unknown")}) has an invalid amount: {invoice.get("amount")}')
            continue

        valid_invoices.append(invoice)
    return valid_invoices


# Two rows are exact duplicates if every field matches.
def remove_duplicatesByRule(invoices, duplicates) -> list[dict]:
    print(f'Removing duplicates from {len(invoices)} invoices')
    seen = set()
    result = []

    for inv in invoices:
        # Convert dict to a hashable tuple of sorted key/value pairs
        duplicates = tuple(sorted(inv.items()))

        if duplicates in seen:
            # duplicate → skip
            continue

        seen.add(duplicates)
        result.append(inv)

    return result
   


# Two rows are suspected duplicates if the vendor, amount and date match but the invoice_id differs.
# Print them as pairs, (INV-107 ~ INV-101), and remove the later row (the first one seen is kept).
def remove_suspected_duplicates(invoices) -> list[dict]:
    print(f'Removing suspected duplicates from {len(invoices)} invoices')
    if invoices is None:
        return [] 

    result_invoices = []
    for invoice in invoices:
        match = None
        for kept in result_invoices:
            if (
                invoice.get("vendor") == kept.get("vendor")
                and invoice.get("amount") == kept.get("amount")
                and invoice.get("date") == kept.get("date")
                and invoice.get("invoice_id") != kept.get("invoice_id")
            ):
                match = kept
                break

        if match is not None:
            print(f'({invoice.get("invoice_id")} ~ {match.get("invoice_id")})')
        else:
            result_invoices.append(invoice)
    return result_invoices


def group_by_vendor(invoices)-> dict[str, list[dict]]:
    print(f'Grouping {len(invoices)} invoices by vendor')
    trueInvoices = clean_invoices(invoices)
    grouped = {}
    invoiceById = {}
    for invoice in trueInvoices:
        vendor = invoice["vendor"]

        if vendor not in grouped:
            grouped[vendor] = []

        grouped[vendor].append(invoice)
    return grouped

#Credit notes. Match each negative invoice to its positive partner. Mark both as "CANCELLED" and exclude them from totals. Print the index pair, for example 3 <-> 6. Handle a credit note with no partner.
def handle_credit_notes(allInvoice) -> list[dict]:
    print(f'Handling credit notes for {len(allInvoice)} invoices')
    grouped = group_by_vendor(allInvoice)
    
    for vendor, invoices in grouped.items():
        totalPayable = 0
        for index, invoice in enumerate(invoices):
            if invoice["amount"] is not None :
                totalPayable += invoice["amount"]
        if totalPayable == 0:
            print("Below paired invoices are cancelled:")
            for invoice in invoices:
                print(f'{invoice.get("invoice_id")}')
                invoice["status"] = "CANCELLED"
                invoice["amount"] = 0
        else:
            print(f'Total payable for vendor {vendor}: {totalPayable}')
    return allInvoice


def reconcile_invoices() -> list[Invoice]:
    print(f'Starting invoice reconciliation')
    invoices = get_Invoices()
    print(f'Retrieved {len(invoices)} invoices')
    cleaned_invoices = clean_invoices(invoices)
    handled_invoices = handle_credit_notes(cleaned_invoices)
    return perform_reconciliation(handled_invoices)


# Reconcile payments. Join payments to invoices by invoice_id. Sum the payments for each invoice. Then print:
def perform_reconciliation(handledInvoices) -> list[Invoice]:
    print(f'Performing reconciliation for {len(handledInvoices)} invoices')
    reconcilation = []
    for invoice in handledInvoices:
        if invoice.get("status") != "CANCELLED":
            payments = get_payments_by_invoice_id(invoice.get("invoice_id"))
            if payments:
                total_paid = 0
                for payment in payments:
                    paid_amount = payment["paid"]
                    if paid_amount is not None and paid_amount > 0:
                        total_paid += paid_amount
                balance = invoice.get("amount", 0) - total_paid
                if total_paid >= invoice.get("amount", 0):
                    invoice["status"] = "PAID"
                else:
                    invoice["status"] = "PARTIALLY_PAID"
            else:
                invoice["status"] = "PENDING"
            print(f'Invoice {invoice.get("invoice_id")} status: {invoice.get("status")}')
        reconcilation.append(invoice)
    return [Invoice(**inv) for inv in reconcilation]


# Other getters and utility functions for invoices can be added below.

def get_Invoices() -> list[dict]:
    return invoiceRepo.get_all()

def get_invoice_by_id(invoice_id) -> Invoice:
  invoices = invoiceRepo.get_all()
  for inv in invoices:
      if inv.get("invoice_id") == invoice_id:
          return Invoice(**inv)
  return {"error": "Invoice not found"}

def delete_invoice_by_id(invoice_id) -> dict:
    success = invoiceRepo.delete_by_id(invoice_id)
    if success:
        return {"message": "Invoice deleted successfully"}
    else:
        return {"error": "Invoice not found"}

def update_invoice_by_id(invoice_id, updated_invoice) -> Invoice:
    updated = invoiceRepo.update_by_id(invoice_id, updated_invoice)
    if updated:
        return Invoice(**updated)
    return {"error": "Invoice not found"}

def add_invoice(new_invoice) -> Invoice:
    invoiceRepo.add_invoice(new_invoice)
    return Invoice(**new_invoice)

def get_payments_by_invoice_id(invoice_id) -> list[dict]:
    return paymentRepo.get_payment_by_invoice_id(invoice_id)
