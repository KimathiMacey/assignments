def calculate_bill():
    customer_id = input("Enter Customer ID: ")
    customer_name = input("Enter Customer Name: ")
    units = int(input("Enter Units Consumed: "))

    if units < 200:
        charges_per_unit = 1.20
    elif units >= 200 and units < 400:
        charges_per_unit = 1.50
    elif units >= 400 and units < 600:
        charges_per_unit = 1.80
    else:
        charges_per_unit = 2.00

    total_bill = units * charges_per_unit

    if total_bill > 400:
        charge = total_bill * 0.15
        total_bill += charge

    if total_bill < 100:
        total_bill = 100

    print("Customer ID:", customer_id)
    print("Customer Name: ", customer_name)
    print("Charges per Unit:", charges_per_unit)
    print("Total Amount to pay", total_bill)

calculate_bill()