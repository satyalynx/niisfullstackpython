#RETURN VALUE WITHOUT ARGUMENT

def add():
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter another number: "))
    s = n1 + n2
    return s

result = add()
print("Sum:", result)