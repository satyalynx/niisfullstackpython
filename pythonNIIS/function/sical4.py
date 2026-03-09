#RETURN VALUE WITHOUT ARGUMENT

def sical():
    p = float(input("Enter principle: "))
    r = float(input("Enter rate of interest: "))
    t = float(input("Enter time: "))
    si = p*r*t/100
    return si

ans = sical()
print("Simple interest: ", ans)