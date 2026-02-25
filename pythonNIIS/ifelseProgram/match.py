'''wap take two number keyboard enter your chaice 
1. add, 
2. sub, 
3. multi, 
invalid choice menu driven program using match case.'''

print("enter two number: ")
n1 = int(input())
n2 = int(input())
print("Enter your choice\n 1.add\n 2.sub\n 3.multi")
ch=int(input())
match ch:
	case 1:print("sum: ", n1+n2)
    case 2:print("sum: ", n1-n2)
    case 3:print("sum: ", n1*n2)
	case _ :print("Invalid choice.")
else:
	print("Invalid choice.")