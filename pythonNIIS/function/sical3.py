#RETURN VALUE WITH ARGUMENT

def sical(p, r, t):
    si = p*r*t/100
    return si

p = float(input("Enter principle: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))
res = sical(p, r, t)
print("Simple interest: ", res)