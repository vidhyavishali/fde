def determine_approval(invoice_amount):
    """
    Determines whether an invoice amount is approved or not.

    Parameters:
    invoice_amount (float): The amount of the invoice.

    Returns:
    str: 'Manager approval required' if the invoice amount is greater than 1000, 'Supervisor approval required' if it's greater than 500, 'Standard approval' otherwise.
    """
    if invoice_amount > 1000:
        return 'Manager approval required'
    elif invoice_amount > 500:
        return 'Supervisor approval required'
    else:
        return 'Standard approval'


approval_status = determine_approval(750)
print(approval_status)  # Output: Supervisor approval required
