#Simple interest program by taking input

#NO RETURN VALUE WITH ARGUMENT
def sical(p, r, t):
	si = p*r*t/100
	print("Simple interest: ", si)
p = float(input("Enter principle: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))
sical(p, r, t)