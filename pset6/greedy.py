import cs50

while True:
    x = float(input("How much change do I owe you? Please enter in dollars.(No negative numbers)\n"))
    if x>0:
        break
x=round(x*100)
quarter=0
dime=0
nickel=0
penny=0
  
while x>=25: 
    x=x-25
    quarter+=1
while x>=10:  
    x=x-10
    dime+=1
while x>=5:
    x=x-5
    nickel+=1
while x>=1:
    x=x-1
    penny+=1
print(quarter+dime+nickel+penny,"\n")
