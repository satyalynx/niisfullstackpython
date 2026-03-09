#Here we are calculating simple interest


class Simple:
	def __init__(self, p, r, t):
		self.p=p
		self.rate=r
		self.time=t
	def show(self):
		print("Principle: ", self.p)
		print("Rate: ", self.rate)
		print("Time: ", self.time)
	def sical(self):
		return self.p*self.rate*self.time/100
print("Enter principle rate and time: ")
#s=Simple(float(input()), float(input()), float(input()))
pr=float(input())
r=float(input())
t=float(input())
s=Simple(pr,r,t)
s.show()
print("Simple Interest: ", s.sical())




















"""class Sical:
	def __init__(self, p, r, t):
		self.principal=p
		self.rate=r
		self.time=t
		self.si=p*r*t/100
	def show(self):
		print("Principal: ", self.principal)
		print("Rate: ", self.rate)
		print("Time: ", self.time)
		print("Simple interest: ", self.si)
s=Sical(5000, 5, 1)
s.show()"""
