#Wap take a oerson x from keyboard check person is eligible for voting or not.
## by ternary operator

print("Enter your age: ")
age = int(input())
msg = "You are eligible." if age>=18 else "You are not eligible."
print(msg)