#RETURN VALUE WITHOUT ARGUMENTS

def facttest():
    num = int(input("Enter a number: "))
    f = 1
    while num > 0:
        f = f * num
        num = num - 1
    return result              

res = facttest()                   
print("Factorial =", res)