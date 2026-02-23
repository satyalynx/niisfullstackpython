# bitwise operator

# |
# &
# ^	xor
# <<
# >>
# ~
# only integer works

# |
# 1	1 	1
# 1	0	1
# 0	1	1
# 0	0	0

# &
# 1	1	1
# 1	0	0
# 0	1	0
# 0	0	0	

# ^
# 1	1	0
# 1	0	1
# 0	1	1
# 0	0	0

print(4 | 7)
print(4 & 7)
print(4 ^ 7)
print("\n")
#practice question
print(14 | 17)
print(14 & 17)
print(14 ^ 17)

print(12>>2)


#~
print(~5)
print(~20)
print(~-12)
print(~0)


a=10
b=3

c=a+ ~b+1
print(c)