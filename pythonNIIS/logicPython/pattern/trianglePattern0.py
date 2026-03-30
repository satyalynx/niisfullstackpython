# Triangle Patterns (Nested Loop)

"""
i -> rows control karta hai
j -> columns control karta hai
i ke hisaab se j ka range change hota hai
"""

# increasing number triangle
"""
1
1    2
1    2    3
1    2    3    4
"""
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="\t")
    print()
print("\n")


# decreasing number triangle
"""
1    2    3    4
1    2    3
1    2
1
"""
for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print(j, end="\t")
    print()
print("\n")


# decreasing character triangle
"""
A    B    C    D
A    B    C
A    B
A
"""
for i in range(68, 64, -1):
    for j in range(65, i + 1):
        print(chr(j), end="\t")
    print()
print("\n")


# increasing character triangle
"""
A
A    B
A    B    C
A    B    C    D
"""
for i in range(65, 69):
    for j in range(65, i + 1):
        print(chr(j), end="\t")
    print()
print("\n")