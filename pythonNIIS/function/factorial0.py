#NO RETURN VALUE WITH ARGUMENT

def factTest(num):
	f = 1
	while num > 0:
		f = f * num
		num = num - 1
	print("Factorial= ", f)
num = int(input("Enter a number: \n"))
factTest(num)