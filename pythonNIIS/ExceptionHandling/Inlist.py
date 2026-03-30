#Exception handling in list and dict

#Example1.1
L=[10,20,30]
try:
	print(L[3])
except IndexError:
	print("index out of range")
print("program end")




#Example1.2
d={1:"A",3:"B"}
try:
	print(d[4])
except KeyError:
	print("key not found")
print("program end")

