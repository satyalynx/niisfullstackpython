#Understanding nested exception

#Example2.1
L=[10,5,7,6]
try:
	print(L[2]/2)
except IndexError:
	print("index error")
except ZeroDivisionError:
	print("zero division error")
print("program end")




#Example2.2
L=[10,5,7,6]
try:
	print(L[2]/0)
except IndexError:
	print("index error")
except ZeroDivisionError:
	print("zero division error")
print("program end")



#Example2.3
L=[10,5,7,6]
try:
	print(L[4]/0)
except IndexError:
	print("index error")
except ZeroDivisionError:
	print("zero division error")
print("program end")



#Example2.4
L=[10,5,7,6]
try:
	print(L[4]/0)
except:
	print("handle all type")
except IndexError:
	print("index error")
except ZeroDivisionError:
	print("zero division error")
print("program end")




#Example2.5
L=[10,5,7,6]
try:
	print(L[4]/0)
except IndexError:
	print("index error")
except ZeroDivisionError:
	print("zero division error")
except:
	print("handle all type")
print("program end")