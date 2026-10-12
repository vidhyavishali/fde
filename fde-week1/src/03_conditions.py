



#class room activity for condition

invoice_amount =50005

approver= {"l1":"Supervisor", "l2" : "Manager", "l3":"Director"}

print("------------Required Approvals - If ----------")

if invoice_amount < 1000 and invoice_amount <= 25000  :
    print(f"{approver['l1']}")
elif invoice_amount >= 25000 :
    if(invoice_amount > 50000) :
       print(f"{approver['l3']}")
    print(f"{approver['l2']}")


print("------------Required Approvals - Match ----------")
match invoice_amount :

    case n if invoice_amount > 25000 :
        if (invoice_amount > 50000) :
          print(f"{approver['l3']}")
        print(f"{approver['l2']}")
    case n if invoice_amount < 1000 and invoice_amount <= 25000  :
        print(f"{approver['l1']}")
    case _:
        print ("default")

