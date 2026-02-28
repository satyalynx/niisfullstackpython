#RETURN VALUE WITH ARGUMENT 

def factorial(num):
    """Return the factorial of `num` (num >= 0)."""
    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result                     # <-- return the computed value


# ---- Example usage ----
n = int(input("Enter a number: "))
ans = factorial(n)                   # receive the returned value
print("Factorial =", ans)            # print it outside the function