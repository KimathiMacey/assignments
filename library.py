bookID = input("Enter Book ID: ")
dueDate = input("Enter due date (YYYY-MM-DD): ")
returnDate = input("Enter return date (YYYY-MM-DD): ")

# calculate days overdue
from datetime import datetime
due_date = datetime.strptime(dueDate, "%Y-%m-%d")
return_date = datetime.strptime(returnDate, "%Y-%m-%d")
days_overdue = (return_date - due_date).days

# calculate fine amount
if days_overdue <= 7:
    fine_rate = 20
elif days_overdue <= 14:
    fine_rate = 50
else:
    fine_rate = 100

fine_amount = days_overdue * fine_rate

# Display results
print("BookID:", bookID)
print("Due Date:", dueDate)
print("Return Date:", returnDate)
print("Days Overdue:", days_overdue)
print("Fine Rate:", fine_rate)
print("Fine Amount", fine_amount)