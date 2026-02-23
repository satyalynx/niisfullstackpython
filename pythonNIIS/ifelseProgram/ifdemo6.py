"""Wap to take emp salary from keyboard if sal>=5000 da=30% hra=20% 
then display basic salary da hra and total salary"""

print("Enter a Basic Salary: ")
sal = int(input())
hra,da = 0,0
if sal>=5000:
	da = sal*30/100
	hra = sal*20/100
total = sal+da+hra
print("Basic salary: ", sal)
print("da: ", da)
print("hra: ", hra)
print("Total salary: ", total)