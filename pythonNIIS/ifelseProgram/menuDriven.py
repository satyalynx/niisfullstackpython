'''wap take two number keyboard enter your chaice 1. add, 2. sub, 3. multi, invalid choice menu driven program'''

print("enter two number: ")
n1 = int(input())
n2 = int(input())
print("Enter your choice\n 1.add\n 2.sub\n 3.multi")
ch=int(input())
if ch==1:
	print("sum: ", n1+n2)
elif ch==2:
	print("sub: ", n1-n2)
elif ch==3:
	print("multi: ", n1*n2)
else:
	print("Invalid choice.")