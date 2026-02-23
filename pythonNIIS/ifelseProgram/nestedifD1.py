#check no. is 2 digit number.
print("Enter a number: ")
num = int(input())
if num<0:
	num=-num
if 10<=num<=99:  #num>=10 and num<=99  
		print("2 digit number.")

#let's do this within a single line (logic)
'''10<=abs(num)<=99'''