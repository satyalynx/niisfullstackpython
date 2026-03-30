# 2D Pattern Printing (Nested Loops)

# 1. Same numbers in each row
# Output:
# 1    2    3    4
# 1    2    3    4
# 1    2    3    4
for i in range(1, 4, 1):
    for j in range(1, 5, 1):
        print(j, end="\t")
    print()
print("\n")


# 2. Row-wise same number
# Output:
# 1    1    1    1
# 2    2    2    2
# 3    3    3    3
for i in range(1, 4, 1):
    for j in range(1, 5, 1):
        print(i, end="\t")
    print()
print("\n")


# 3. Reverse row-wise numbers
# Output:
# 3    3    3    3
# 2    2    2    2
# 1    1    1    1
for i in range(3, 0, -1):
    for j in range(1, 5, 1):
        print(i, end="\t")
    print()
print("\n")


# 4. Same characters in each row
# Output:
# A    B    C    D
# A    B    C    D
# A    B    C    D
for i in range(1, 4, 1):
    for j in range(65, 69, 1):
        print(chr(j), end="\t")
    print()

# Alternative way (same output)
for i in range(65, 68, 1):
    for j in range(65, 69, 1):
        print(chr(j), end="\t")
    print()
print("\n")


# 5. Row-wise same characters
# Output:
# A    A    A    A
# B    B    B    B
# C    C    C    C
for i in range(65, 68, 1):
    for j in range(65, 69, 1):
        print(chr(i), end="\t")
    print()
print("\n")


# 6. Reverse characters in each row
# Output:
# D    C    B    A
# D    C    B    A
# D    C    B    A
for i in range(67, 64, -1):
    for j in range(68, 64, -1):
        print(chr(j), end="\t")
    print()
print("\n")


# 7. Reverse row-wise characters
# Output:
# C    C    C    C
# B    B    B    B
# A    A    A    A
for i in range(67, 64, -1):
    for j in range(68, 64, -1):
        print(chr(i), end="\t")
    print()
print("\n")


# Important Notes:

# 1. Outer loop (i) = rows control karta hai
# 2. Inner loop (j) = columns control karta hai
# 3. print() = next line ke liye
# 4. chr() = ASCII to character conversion
# 5. Logic change karo -> pattern change ho jayega