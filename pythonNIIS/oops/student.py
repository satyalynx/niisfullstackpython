#Here we are taking 2 students data using class and object

class Student:
	def __init__(self, n, r, m):
		self.name=n
		self.roll=r
		self.mark=m 
	def show(self):
		print("my name: ", self.name)
		print("my roll no: ", self.roll)
		print("my mark: ", self.mark)
s1=Student("Satya", 1, 90)
s2=Student("Ashmita", 2, 80)
s1.show()
s2.show()