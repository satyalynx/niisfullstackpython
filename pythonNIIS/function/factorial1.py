#RETURN VALUE WITH ARGUMENT 

def factorial(num):
    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result                    

n = int(input("Enter a number: "))
ans = factorial(n)                   
print("Factorial =", ans)           