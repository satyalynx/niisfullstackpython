# Program: Electricity Bill Calculation
# Assume the following rates:

# Units Consumed	Rate per Unit
# 0 - 100	₹1.5
# 101 - 200	₹2.5
# 201 - 300	₹4.0
# Above 300	₹6.0


# Electricity Bill Calculator

units = int(input("Enter total electricity units consumed: "))
bill = 0

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1.5) + (units - 100) * 2.5
elif units <= 300:
    bill = (100 * 1.5) + (100 * 2.5) + (units - 200) * 4.0
else:
    bill = (100 * 1.5) + (100 * 2.5) + (100 * 4.0) + (units - 300) * 6.0

print("Total Bill = ₹", round(bill, 2))