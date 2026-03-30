#Demo what we do before
def divide(no1,no2):
	print("divide start")
	print(no1/no2)
	print("divide end")
print("main start")
divide(10,2)
print("main end")



#Here
def divide(no1,no2):
	print("divide start")
	print(no1/no2)
	print("divide end")
print("main start")
divide(10,2)
divide(10,0)
print("main end")




#Example4.1
def divide(no1,no2):
	print("divide start")
	try:
		print(no1/no2)
	except:
		print("caught")
	print("divide end")
print("main start")
divide(10,2)
divide(10,0)
print("main end")



#Example4.2
def divide(no1,no2):
	print("divide start")
	print(no1/no2)
	print("divide end")
print("main start")
divide(10,2)
try:
	divide(10,0)
except:
	print("exceptio hadle")
print("main end")