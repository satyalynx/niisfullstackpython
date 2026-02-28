#RETURN VALUE WITH ARGUMENT

def check(n):
    if n%2==0:
        return "Even number."
    else:
        return "Odd number."

n = int(input("Enter a number: "))
result = check(n)
print(result)