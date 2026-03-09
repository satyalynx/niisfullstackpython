#Here the rectangle program

class rectangle:
	def __init__(self, l, b):
		self.length=l 
		self.breadth=b
	def show(self):
		print("Length: ", self.length)
		print("Breadth: ", self.breadth)
	def perimeter(self):
		return 2*(self.length+self.breadth)
	def area(self):
		return self.length*self.breadth
print("Enter two numbers: ")
rec=rectangle(float(input()), float(input()))
print("perimeter: ", rec.perimeter())
print("Area: ", rec.area())

