"""Wap to take emp salary from keyboard if sal>=5000 da=30% hra=20%  sal<5000 da=20% hra=10%
then display basic salary da hra and total salary"""

print("Enter a Basic Salary: ")
sal = int(input())
hra,da = 0,0
if sal>=5000:
	da = sal*0.3
	hra = sal*0.2
else:
	da=sal*0.2
	hra=sal*0.1
total = sal+da+hra
print("Basic salary: ", sal)
print("da: ", da)
print("hra: ", hra)
print("Total salary: ", total)