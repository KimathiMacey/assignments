def eligibility():
    # User inputs age
    age = int(input("Enter your age: "))
    # input citizenship status
    citizen = input("Are you a Kenyan citizen? (yes/no) ")
    # check eligibility function
    if age >= 18 and citizen.lower() == "yes":
        return True
    else:
        return False
# check eligibility and print result
if eligibility():
    print("You are eligible to vote in the Kenya.")
else:
    print("You are not eligible to vote in Kenya.")