#display indicideual letter line by line using range but backwards

#first way --
s = "Welcome"
for i in range(-1,-8,-1):
	print(s[i])


#second way --
s = "Welcome back"
for i in range(-1,-len(s)-1,-1):
	print(s[i])


#third way --
s = "Welcome back"
for i in range(len(s)-1,-1,-1):
	print(s[i])