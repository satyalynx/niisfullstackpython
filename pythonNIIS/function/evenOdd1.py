#RETURN VALUE WITHOUT ARGUMENT

def check():
    n = int(input("Enter a number: "))
    if n%2==0:
        return "Even number."
    else:
        return "Odd number."

result = check()
print(result)