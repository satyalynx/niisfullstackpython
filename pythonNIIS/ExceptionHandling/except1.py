#Example1
print("A")
try:
	print(10//2)
	print("end try block")
except:
	print("exception handle ")
print("program end")


#Example2
print("A")
try:
	print("try start")
	print(10//0)
	print("end try block")
except:
	print("exception handle ")
print("program end")


#Example3
print("A")
try:
	print("try start")
	print(10//2)
	print("end try block")
except:
	print("exception handle ")
print("program end")



#Example4
print("A")
try:
	print("try start")
	print(10//0)
	print("end try block")
except Exception:
	print("exception handle  all type")
print("program end")


#Example5
print("A")
try:
	print("try start")
	print(10//0)
	print("end try block")
except BaseException:
	print("exception handle  all type")
print("program end")



#Example6
print("A")
try:
	print("try start")
	print(10//0)
	print("end try block")
except ZeroDivisionError:
	print("exception handle")
print("program end")



#Example7
print("A")
try:
	print("try start")
	print(10//0)
	print("end try block")
except IndexError:
	print("exception handle")
print("program end")
