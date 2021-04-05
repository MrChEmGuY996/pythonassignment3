
# 1 enter first and last name
# 2 enter phone number and email
# 3 enter the down payment for the car

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = (first_name +" " + last_name)
# 1 enter first and last name

customers_phone_number = input("enter the customer's phone number: ")

customers_e_mail = input("enter the customer's E-mail: ")
# 2 enter phone number and email

price = 10000

has_good_credit = True
if has_good_credit:
    down_payment = 0.1*price
else:
    down_payment = 0.2 * price

# 3 enter the down payment for the car

print("Full Names: " + full_name)
print("Phone: " + customers_phone_number)
print("E-mail: " + customers_e_mail)
print("Down payment: " + str(down_payment))
