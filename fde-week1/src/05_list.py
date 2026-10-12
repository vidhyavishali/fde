

invoice1 = [{ "customer":"Max Müller", "amount":5000, "status":"pending"},
            { "customer":"drek Ramson", "amount":5000, "status":"approved"},
            { "customer":"John Meyer", "amount":5000000, "status":"rejected"}]



for invoice in invoice1:
    print(f"{invoice['customer']} applied for {invoice['amount']}. The status is {invoice['status']}")




 #List of employee id, name, salary and then print only those names with length > 6 and salary < 250000

employees = [{ "emp":"Max Müller", "id":1, "salary":10000},
            { "emp":"drek Ramson", "id":2, "salary":260000},
            { "emp":"John", "id":3, "salary":255000}]

for em in employees:
    if len(em['emp']) > 6 and em['salary'] > 250000 :
        print(f" {em['emp']} of empid = { em['id']} has salary - {em['salary']}" )
