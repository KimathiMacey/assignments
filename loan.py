# Prompt the user for their age
age = int(input("Please enter your age: "))
# Prompt the user for their annual income
income = int(input("Please enter your annual income: "))
# Check if the user is eligible for a loan
if age >= 21 and income >= 21000:
   print("Congratulations, you qualify for a loan")
else:
   print("Unfortunately, we are unable to offer you a loan at this time.")
