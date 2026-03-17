#Userdefined exception 

class VoteError(BaseException):
	def __init__(self, name):
		super().__init__()
print("enter a age: ")
age = int(input())
if age >= 18:
	print("eligible")
else:
	try:
		raise VoteError("age not allow.")
	except:
		print("not allow")
print("main end")