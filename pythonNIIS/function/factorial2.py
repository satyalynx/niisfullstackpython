#RETURN VALUE WITHOUT ARGUMENTS

def factorial():
    """Prompt the user for a number, compute its factorial and return it."""
    num = int(input("Enter a number: "))
    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result                     # <-- return the computed value


# ---- Example usage ----
ans = factorial()                     # the input happens inside the function
print("Factorial =", ans)