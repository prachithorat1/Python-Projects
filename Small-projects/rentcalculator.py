#INPUT
# Input to take from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit
# Persons living in the room/flat

#OUTPUT
# Total amount you have to pay


rent = int(input("Enter your hostel/flat rent ="))
food = int(input("Enter the amount of food ordered ="))
electricity_spend = int(input("Enter the total of electricity spend ="))
charge_per_unit = int(input("Enter the charge per unit ="))
persons = int(input("Enter the number of persons living in room/flat ="))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person will pay = ", output)

# Enter your hostel/flat rent =5000
# Enter the amount of food ordered =2000
# Enter the total of electricity spend =300
# Enter the charge per unit =10
# Enter the number of persons living in room/flat =4
# Each person will pay =  2500
