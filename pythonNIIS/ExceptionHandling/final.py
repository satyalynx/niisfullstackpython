#Example3.1
L=[10,5,7,6]
try:
	print(L[2]/2)
finally:
	print("must exceute")
print("program end")



#Example3.2
L=[10,5,7,6]
try:
	print(L[2]/0)
finally:
	print("must exceute")
print("program end")




#Exampe3.3
L=[10,5,7,6]
try:
	print(L[2]/0)
except:
	print("exception handle")
finally:
	print("must exceute")
print("program end")