#wap take a number from keyboard check no is sd dd td od +ve number check

print("Enter a number: ")
num = int(input())
if num<0:
	if num<10:
		print("sd")
	elif num<100:
		print("dd")
	elif num<1000:
		print("td")
	else:
		print("od")
else:
	print("enter a +ve number.")