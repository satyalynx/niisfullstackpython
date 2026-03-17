# STRING OPERATORS IN PYTHON


# 1. Concatenation Operator (+)
# Used to combine two or more strings

a = "Hello"
b = "World"
print(a + " " + b)   # Hello World



# 2. Repetition Operator (*)
# Used to repeat a string multiple times

text = "Hi "
print(text * 3)      # Hi Hi Hi 



# 3. Membership Operators (in, not in)
# Used to check whether a substring exists in a string

s = "Python Programming"
print("Python" in s)       # True
print("Java" not in s)     # True



# 4. Comparison Operators
# (==, !=, <, >, <=, >=)
# Used to compare strings (dictionary order)

print("apple" == "apple")    # True
print("apple" < "banana")    # True
print("cat" != "dog")        # True



# 5. String Slicing / Indexing
# Used to access characters or parts of a string

s = "Python"
print(s[0])     # P
print(s[1:4])   # yth



# 6. Escape Characters (\)
# Used to include special characters

print("He said, \"Hello!\"")   # He said, "Hello!"
print("Line1\nLine2")          # New line



# 7. Assignment Operators with Strings (+=, *=)

s = "Hello"
s += " World"
print(s)          # Hello World

s = "Hi "
s *= 3
print(s)          # Hi Hi Hi 



# 8. String Formatting using % operator

name = "Alice"
age = 25
ht = 5.6

print("Name: %s, Age: %d, Height: %f" % (name, age, ht))

# %s -> string
# %d -> integer
# %f -> float



# 9. f-Strings (modern method)

name = "Bob"
age = 30

print(f"My name is {name} and I'm {age} years old.")



# 10. Logical Operators with Strings

print("" and "Hello")       # ""
print("Hi" and "Hello")     # Hello

print(3 and 5)              # 5
print(3 > 0 and 5 > 0)      # True

print("" or "World")        # World



# 11. Identity Operators (is, is not)

a = "hello"
b = "hello"
print(a is b)   # True



# 12. Ternary Operator

x = 5
result = "Even" if x % 2 == 0 else "Odd"
print(result)   # Odd



# 13. Mixed Example

a = "Code"
b = "Fun"

print(a + b)        # CodeFun
print(a * 2)        # CodeCode
print("C" in a)     # True
print(a == b)       # False
# print(a + 3)      # error



# 14. Practice Example

s = "ram"
print(s * 3)

s1 = "das"
print(s + s1)

print('a' in s1)
print('x' in s1)

s2 = "abc"
s3 = "Abc"

print(s2 == s3)
print(s2 >= s3)
print(s2 <= s3)
print(s2 != s3)



# 15. Count characters using len()

s = "welcome"
print(len(s))
print(len("ok"))



# 16. Count characters without len()

s = "welcome"
c = 0

for i in s:
    c = c + 1

print("No of characters =", c)