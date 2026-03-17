# write a program to take a string from keyboard and count:
# number of characters, alphabets, uppercase, lowercase,
# vowels, consonants, digits, spaces, symbols and words

print("enter a string ")
s = input()
alp, lw, up, vw, co, dg, sp, wd, c, sy=0, 0, 0, 0, 0, 0, 0, 0, 0, 0
for i in s:
    if i.isalpha():
        alp = alp + 1
        if i.isupper():
            up = up + 1
        else:
            lw = lw + 1
        if i in "aeiouAEIOU":
            vw = vw + 1
        else:
            co = co + 1 
    elif i.isdigit():
        dg = dg + 1
    elif i.isspace():
        sp = sp + 1
    else:
        sy = sy + 1
    c = c + 1
wd = sp + 1

print("total no of char =", c)
print("total no of alphabet =", alp)
print("total no of vowel =", vw)
print("total no of consonant =", co)
print("total no of uppercase =", up)
print("total no of lowercase =", lw)
print("total no of digit =", dg)
print("total no of space =", sp)
print("total no of symbol =", sy)
print("total no of words =", wd)




