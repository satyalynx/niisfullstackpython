#Convert uppercase to lowercase
import sys 

print("Enter a character: ")
ch = input()
if len(ch)>1:
	print("only one character is allowed.")
	sys.exit()
if ch>='A' and ch<='Z':
	ch=chr(ord(ch)+32)
	print(ch)