# Parent class
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show_person(self):
		print("Name:", self.name)
		print("Age:", self.age)


# Child class
class Student(Person):
	def __init__(self, name, age, roll):
		super().__init__(name, age)   # calling parent constructor
		self.roll = roll

	def show_student(self):
		print("Roll no.:", self.roll)


# Grandchild class
class EnggStudent(Student):
	def __init__(self, name, age, roll, branch):
		super().__init__(name, age, roll)   # calling parent constructor
		self.branch = branch

	def show_enggStudent(self):
		print("Branch:", self.branch)


# Object creation
e = EnggStudent("Satya", 21, 43, "Computer Science")

# Calling methods
e.show_person()
e.show_student()
e.show_enggStudent()