#factorial of number
''' 3! = 3*2*1 = 6
	4! = 4*3*2*1 = 24
	0! = 1
	1! = 1 '''

#NO RETURN VALUE WITH NO ARGUMENT
#normal factorial 
'''num = 4
f = 1
while num > 0:
	f = f * num:
	num = num - 1
print("Factorial= ", f)'''


#with function
def factTest():
	num = int(input("Enter a number: \n"))
	f = 1
	while num > 0:
		f = f * num
		num = num - 1
	print("Factorial= ", f)
factTest()