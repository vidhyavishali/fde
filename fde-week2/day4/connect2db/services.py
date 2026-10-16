import paymentRepository as payRepo


def get_all_payments_service():
   return  payRepo.get_all_payments()

def get_payment_by_id_service(payment_id):
    return payRepo.get_payment_by_id(payment_id)

def add_payment_service(recipient, amount, status, transactionid):
    payRepo.add_payment(recipient, amount, status, transactionid)

def delete_payment_service(payment_id):
    payRepo.delete_payment(payment_id)

def update_payment_service(payment_id, updated_payment):
    payRepo.update_payment(payment_id, updated_payment)

