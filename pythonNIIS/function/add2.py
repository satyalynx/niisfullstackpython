#NO RETURN VALUE WITH ARGUMENT

''' def add(n1, n2):
	s=n1+n2
	print("sum: ", s)
	return
add(10, 20) '''

#taking user input
def add (n1, n2):
	s = n1+n2
	print("sum: ", s)
	return
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
add(n1, n2)