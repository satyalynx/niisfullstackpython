
class myTime:
	def __init__(self, h, m, s):
		self.h = h
		self.m = m
		self.s = s

	def __gt__(self, t2):
		if self.h != t2.h:
			return self.h > t2.h
		elif self.m != t2.m:
			return self.m > t2.m 
		else:
			return self.m > t2.m 

	def show(self):
		print(self.h, ":", self.m, ":", self.s)

print("Enter time for t1")
h1 = int(input("Enter hours: "))
m1 = int(input("Enter minutes: "))
s1 = int(input("Enter seconds: "))

print("Enter time for t2")
h2 = int(input("Enter hours: "))
m2 = int(input("Enter minutes: "))
s2 = int(input("Enter seconds: "))

t1 = myTime(h1, m1, s1)
t2 = myTime(h2, m2, s2)

print("\nTime 1: ")
t1.show()

print("\nTime 2: ")
t2.show()


if t1 > t2:
	print("t1 is bigger than t2")
elif t2 > t1:
	print("t2 is bigger than t1")
else:
	print("Both times are equal")