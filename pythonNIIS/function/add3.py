#RETURN VALUE WITH ARGUMENT

def add(n1, n2):
    s = n1 + n2
    return s

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
result = add(n1, n2)
print("Sum:", result)