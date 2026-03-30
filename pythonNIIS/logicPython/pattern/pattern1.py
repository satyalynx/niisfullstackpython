# 1	1 1	1	
# 2	2 2	2	
# 3	3 3	3	

for i in range(1,4,1):
	for j in range(1,5,1):
		print(i, end="\t")
	print()

print("\n")


#3 3 3 3
#2 2 2 2 
#1 1 1 1 

for i in range(3,0,-1):
	for j in range(1,5,1):
		print(i, end="\t")
	print()

print("\n")

#3 3 3 3
#2 2 2 2 
#1 1 1 1 

for i in range(3,0,-1):
	for j in range(1,5,1):
		print("i=",i, "j=", j, end="\t")
	print()

print("\n")

# A	A A	A	
# B	B B	B	
# C	C C	C	

for i in range(65,68,1):
	for j in range(1,5,1):
		print(chr(i), end="\t")
	print()

print("\n")

# A	B C	D	
# A	B C	D	
# A	B C	D	

for i in range(65,68,1):
	for j in range(65,69,1):
		print(chr(j), end="\t")
	print()

print("\n")



for i in range(67,64,1):
	for j in range(68,69,1):
		print(chr(j), end="\t")
	print()

print("\n")



for i in range(67,64,-1):
	for j in range(68,64,-1):
		print(chr(i), end="\t")
	print()

print("\n")
