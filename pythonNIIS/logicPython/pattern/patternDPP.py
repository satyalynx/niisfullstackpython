# Pattern Practice Set

# 1.
# 4 3 2 1
# 4 3 2
# 4 3
# 4
for i in range(4, 0, -1):
    for j in range(4, i-1, -1):
        print(j, end="\t")
    print()
print("\n")


# 2.
# 4
# 4 3
# 4 3 2
# 4 3 2 1
for i in range(4, 0, -1):
    for j in range(4, i-1, -1):
        print(j, end="\t")
    print()
print("\n")


# 3.
# D C B A
# D C B
# D C
# D
for i in range(68, 64, -1):
    for j in range(68, i-1, -1):
        print(chr(j), end="\t")
    print()
print("\n")


# 4.
# D
# D C
# D C B
# D C B A
for i in range(68, 64, -1):
    for j in range(68, i-1, -1):
        print(chr(j), end="\t")
    print()
print("\n")


# 5.
# 1
# 2 1
# 3 2 1
# 4 3 2 1
for i in range(1, 5):
    for j in range(i, 0, -1):
        print(j, end="\t")
    print()
print("\n")


# 6.
# A
# B A
# C B A
# D C B A
for i in range(65, 69):
    for j in range(i, 64, -1):
        print(chr(j), end="\t")
    print()
print("\n")


# 7.
# 4 3 2 1
# 3 2 1
# 2 1
# 1
for i in range(4, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="\t")
    print()
print("\n")


# 8.
# D C B A
# C B A
# B A
# A
for i in range(68, 64, -1):
    for j in range(i, 64, -1):
        print(chr(j), end="\t")
    print()
print("\n")


# 9.
# 4
# 3 4
# 2 3 4
# 1 2 3 4
for i in range(4, 0, -1):
    for j in range(i, 5):
        print(j, end="\t")
    print()
print("\n")


# 10.
# 1 2 3 4
# 2 3 4
# 3 4
# 4
for i in range(1, 5):
    for j in range(i, 5):
        print(j, end="\t")
    print()
print("\n")


# 11.
# D
# C D
# B C D
# A B C D
for i in range(68, 64, -1):
    for j in range(i, 69):
        print(chr(j), end="\t")
    print()
print("\n")


# 12.
# A B C D
# B C D
# C D
# D
for i in range(65, 69):
    for j in range(i, 69):
        print(chr(j), end="\t")
    print()
print("\n")