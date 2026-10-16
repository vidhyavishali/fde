from database import get_connection
from models import Payment


"""
This module provides functions to interact with the payments table in the database.
It includes functions to retrieve all payments and to retrieve a payment by its ID.
Steps to connect and interact with the payments table: (CDEF)
1. get connection (C - connection)
2. create cursor object from the connection cursor ( D - define the cursor)
3. execute SQL query ( E - Execute the query)
4. fetch results ( F - Fetch the results)  ( commit in case of writing)
5. close cursor and connection
6. return results as Payment objects

"""
def get_all_payments():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, recipient, amount, status, transactionid FROM payments WHERE deleted = FALSE")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [Payment(id=row[0], recipient=row[1], amount=row[2], status=row[3], transactionid=row[4]) for row in rows]


def get_payment_by_id(payment_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, recipient, amount, status, transactionid FROM payments WHERE id = %s AND deleted = FALSE", (payment_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        return Payment(id=row[0], recipient=row[1], amount=row[2], status=row[3], transactionid=row[4])
    return None

def add_payment(recipient, amount, status, transactionid):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO payments (recipient, amount, status, transactionid) VALUES (%s, %s, %s, %s)",
        (recipient, amount, status, transactionid)
    )
    conn.commit()
    cur.close()
    conn.close()    


def delete_payment(payment_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE payments SET deleted = TRUE WHERE id = %s",
        (payment_id,)
    )
    conn.commit()
    cur.close()
    conn.close()

def update_payment(payment_id, updated_payment):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE payments SET recipient = %s, amount = %s, status = %s, transactionid = %s WHERE id = %s",
        (updated_payment.recipient, updated_payment.amount, updated_payment.status, updated_payment.transactionid, payment_id)
    )
    conn.commit()
    cur.close()
    conn.close()