n=int(input("enter the number:"))
a=n
product=1
s=0
while n!=0:
    r=n%10
    for i in range(r,0,-1):
        product=product*i
    s=s+product
    n=n//10
    product=1
print(s)
if a==s:
    print("krishnamurthy number")
else:
        print("not a krishna murthy num")
    
