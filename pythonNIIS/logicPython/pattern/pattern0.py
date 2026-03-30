# Pattern Printing Basics in Python

# 1. Direct print (hardcoded)
# Output: 1 2 3 4
#         1 2 3 4 5
print("1 2 3 4")
print("1 2 3 4 5")
print("\n")


# 2. Print numbers 1 to 4 using loop
# Output: 1    2    3    4
for j in range(1, 5, 1):
    print(j, end="\t")
print("\n")


# 3. Print numbers 1 to 5
# Output: 1    2    3    4    5
for j in range(1, 6, 1):
    print(j, end="\t")
print("\n")


# 4. Using variable
# Output: 1    2    3    4
r = 4
for j in range(1, r + 1, 1):
    print(j, end="\t")
print("\n")


# 5. Using user input
# Output: depends on user input
r = int(input("Enter value of r: "))
for j in range(1, r + 1, 1):
    print(j, end="\t")
print("\n")


# 6. Reverse numbers 4 to 1
# Output: 4    3    2    1
for j in range(4, 0, -1):
    print(j, end="\t")
print("\n")


# 7. Print stars
# Output: *    *    *    *
for j in range(1, 5, 1):
    print("*", end="\t")
print("\n")


# 8. Print same number
# Output: 1    1    1    1
for j in range(1, 5, 1):
    print("1", end="\t")
print("\n")


# 9. Print characters A to D
# Output: A    B    C    D
for j in range(65, 69, 1):
    print(chr(j), end="\t")
print("\n")


# 10. Reverse characters D to A
# Output: D    C    B    A
for j in range(68, 64, -1):
    print(chr(j), end="\t")
print("\n")