#display indicideual letter line by line using range

#first way --
s = "Welcome"
for i in range(0,7,1):
	print(s[i])


#second way --
s = "Welcome back"
for i in range(0,len(s),1):
	print(s[i])


#third way --
s = "Welcome back"
for i in range(-len(s),0,1):
	print(s[i])