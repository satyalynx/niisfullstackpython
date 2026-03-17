# STRING OPERATORS AND STRING METHODS IN PYTHON


# 1. Concatenation Operator (+)
# Used to combine strings

a = "Hello"
b = "World"
print(a + " " + b)   # Hello World



# 2. Repetition Operator (*)
# Used to repeat string

text = "Hi "
print(text * 3)      # Hi Hi Hi 



# 3. Membership Operators (in, not in)

s = "Python Programming"
print("Python" in s)       # True
print("Java" not in s)     # True



# 4. Comparison Operators

print("apple" == "apple")    
print("apple" < "banana")    
print("cat" != "dog")        



# 5. Indexing and Slicing

s = "Python"
print(s[0])     
print(s[1:4])   



# 6. Escape Characters

print("He said, \"Hello!\"")
print("Line1\nLine2")



# 7. Assignment Operators

s = "Hello"
s += " World"
print(s)

s = "Hi "
s *= 3
print(s)



# 8. String Formatting (% operator)

name = "Alice"
age = 25
ht = 5.6

print("Name: %s, Age: %d, Height: %f" % (name, age, ht))



# 9. f-Strings

name = "Bob"
age = 30

print(f"My name is {name} and I'm {age} years old.")



# 10. Logical Operators

print("" and "Hello")
print("Hi" and "Hello")

print(3 and 5)
print(3 > 0 and 5 > 0)

print("" or "World")



# 11. Identity Operators

a = "hello"
b = "hello"
print(a is b)



# 12. Ternary Operator

x = 5
result = "Even" if x % 2 == 0 else "Odd"
print(result)



# 13. Case Conversion Methods

s = "ram is a Good boy"
print(s.title())

s = "ram is a Good boy"
print(s.capitalize())

s = "ram is a Good boy"
print(s.upper())

s = "rAM is a Good boy"
print(s.lower())

s = "rAM is a Good boy"
print(s.casefold())



# 14. Swap Case

s = "rAM is a Good boy"
print(s.swapcase())



# 15. Removing Spaces

s = " hi"
s = s.lstrip()
print(s)

s = "hi "
s = s.rstrip()
print(s)

s = " hi "
s = s.strip()
print(s)



# 16. Alignment Functions

s = "hi"
print(s.center(5))
print(s.center(5, "*"))
print(s.ljust(5, "*"))
print(s.rjust(5, "*"))



# 17. startswith() and endswith()

s = "ram is a good boy"
print(s.startswith("r"))
print(s.startswith("ram"))
print(s.startswith("rom"))

print(s.endswith("y"))
print(s.endswith("boy"))
print(s.endswith("box"))

print(s.startswith("r", 4))
print(s.startswith("is", 4))
print(s.endswith("o", 4, 11))



# 18. count()

s = "ram is a good is boy"
print(s.count("a"))
print(s.count("is"))
print(s.count("x"))
print(s.count(" "))



# 19. index() and rindex()

s = "ram is a good is boy"
print(s.index("a"))
print(s.index("m"))

print(s.rindex("a"))
print(s.rindex("m"))
# print(s.rindex("x"))   # error



# 20. find() and rfind()

s = "ram is a good is boy"
print(s.find("a"))
print(s.find("m"))
print(s.find("x"))

print(s.rfind("a"))
print(s.rfind("m"))
print(s.rfind("x"))



# 21. replace()

s = "ram is a good boy"
print(s.replace("ram", "shyam"))



# 22. Checking Functions

s = "Ab3"
print(s.isalnum())

s = "Ab#3"
print(s.isalnum())

s = "Ab"
print(s.isalpha())

s = "Ab3"
print(s.isalpha())

s = "125"
print(s.isdigit())

s = "125a"
print(s.isdigit())

s = " "
print(s.isspace())

s = "ram is"
print(s.isspace())

s = "a"
print(s.islower())

s = "B"
print(s.islower())

s = "a"
print(s.isupper())

s = "B"
print(s.isupper())



# 23. Encoding and Decoding

s = "hi"
x = s.encode()
print(type(s), type(x))

s1 = x.decode()
print(s1)



# 24. split() and join()

s = "ram is a good boy"
L = s.split()
print(L)

L = s.split("i")
print(L)

L = s.split()
print(" ".join(L))
print("#".join(L))



# 25. Counting Programs

s = "WelCOme123"

# uppercase
c = 0
for i in s:
    if i.isupper():
        c += 1
print("uppercase =", c)

# lowercase
c = 0
for i in s:
    if i.islower():
        c += 1
print("lowercase =", c)

# digits
c = 0
for i in s:
    if i.isdigit():
        c += 1
print("digits =", c)

# vowels
vw = 0
for i in s:
    if i in "aeiouAEIOU":
        vw += 1
print("vowels =", vw)

# alphabets
c = 0
for i in s:
    if i.isalpha():
        c += 1
print("alphabets =", c)

# spaces
s = "WelCOme123 boy"
c = 0
for i in s:
    if i.isspace():
        c += 1
print("spaces =", c)



# 26. Final Combined Program

s = "WelCOme123 boy"

upper = lower = digit = space = vowel = consonant = 0

for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

    if i.isdigit():
        digit += 1

    if i.isspace():
        space += 1

    if i in "aeiouAEIOU":
        vowel += 1
    elif i.isalpha():
        consonant += 1

print("Uppercase =", upper)
print("Lowercase =", lower)
print("Digits =", digit)
print("Spaces =", space)
print("Vowels =", vowel)
print("Consonants =", consonant)