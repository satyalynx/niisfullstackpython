#raise is used in userdefined exception.

#Example5.1
class NegativeError(BaseException):
	def init(self):
		print("negative number not allow")
print("enter a number ")
no=int(input())
if no<0:
	raise NegativeError()
else:
	print("number=",no)


#Example5.2
class NegativeError(BaseException):
	def init(self):
		print("negative number not allow")
print("enter a number ")
no=int(input())
if no<0:
	raise NegativeError()
else:
	print("number=",no)
print("program end")



#Example5.2
class NegativeError(BaseException):
	def init(self):
		print("negative number not allow")
print("enter a number ")
no=int(input())
if no<0:
	try:
		raise NegativeError()
	except:
		print("exception caught negative number not allow ")
else:
	print("number=",no)
print("program ed")
