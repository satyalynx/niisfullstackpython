# syn4:
# if   c1:
# 	if c2:
# 		c2 true block
# 	else:
# 		c2 false block
# else:
# 	if c3:
# 		c3 true block
# 	else:
# 		c3 false block

#wap take 3 number from keyboard display bigest number
print("enter three nos")
no1=int(input())
no2=int(input())
no3=int(input())
if no1>=no2:
	if no1>=no3:
		print("first number is biger ",no1)
	else:
		print("third number is biger ",no3)
else:
	if no2>=no3:
		print("second no is biger ",no2)
	else:
		print("third no is biger ",no3)