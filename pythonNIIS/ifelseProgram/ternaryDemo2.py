"""Wap to take emp salary from keyboard if sal>=5000 da=30% hra=20%  sal<5000 da=20% hra=10%
then display basic salary da hra and total salary"""

#Using ternary operator

print("enter basic sal: ")
sal=float(input())
da = sal*0.3 if sal>=5000 else sal*0.2
hra = sal*0.2 if sal>=5000 else sal*0.1
totalsal=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total sal=",totalsal)