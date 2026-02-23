#Compound Interest 
principal = float(input())
rate = float(input())
time = float(input())
n = int(input())
ci = principal*(1+rate/n)**(n*time)-principal
print("Compound Interest: ", ci)