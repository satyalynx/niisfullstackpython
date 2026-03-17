#display individual letter line by line using sequence

#first way --
s = "welcome"
for i in s:
	print(i)

print("\n")

#second way --
s = "welcome"
s = s[::-1]
for i in s:
	print(i)
