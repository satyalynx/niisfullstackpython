# INDEXING AND SLICING IN PYTHON


'''
Indexing
String ke characters ko access karne ke liye use hota hai

Example:
'''

s = "welcome"
print(s[3], s[-4])

# print(s[7])   # error: index out of range
# print(s[-8])  # error


'''
Index position:

 0    1    2    3    4    5    6
 w    e    l    c    o    m    e

-7   -6   -5   -4   -3   -2   -1
'''



'''
Slicing
Substring nikalne ke liye use hota hai

Syntax:
[start : stop : step]

[start : stop]
[start :]
[: stop]
[::]

Default:
start = 0
stop = end-1
step = 1
'''


# Example 1

s = "welcome"
print(s[2:5:1])     # lco
print(s[-5:-2:1])   # lco



# Example 2

s = "welcome"

print(s[::])        # welcome
print(s[:])         # welcome
print(s[2:])        # lcome
print(s[2:4])       # lc
print(s[::1])       # welcome
print(s[:10:1])     # welcome
print(s[::2])       # wloe
print(s[:6:2])      # wlo



# Note: slicing in list

s = ["welcome"]
print(s[2:2])       # []
print(s[5:3])       # []



'''
Reverse Slicing Examples
'''

s = "welcome"

print(s[::-1])         # emoclew
print(s[6:3:-1])       # emo
print(s[-1:-4:-1])     # emo
print(s[-3:])          # ome
print(s[-3:-1])        # om
print(s[-3:-1:1])      # om
print(s[-3::-1])       # oclew
print(s[-3:-8:-1])     # oclew
print(s[-3:-100:-1])   # oclew
print(s[:-1])          # welcom
print(s[-7::])         # welcome
print(s[-7::-1])       # w



# WAP: display characters using sequence

s = "welcome"
for i in s:
    print(i)



# WAP: count number of characters

s = "welcome"
print(len(s))



# WAP: display characters using range

s = "welcome"
for i in range(0, len(s), 1):
    print(s[i])



# WAP: display characters using negative range

s = "welcome"
for i in range(-len(s), 0, 1):
    print(s[i])



# WAP: display string in reverse (using slicing)

s = "welcome"
s = s[::-1]

for i in s:
    print(i)



# WAP: display string in reverse (using range)

s = "welcome"
for i in range(len(s) - 1, -1, -1):
    print(s[i])



# WAP: display string in reverse (using negative range)

s = "welcome"
for i in range(-1, -len(s) - 1, -1):
    print(s[i])