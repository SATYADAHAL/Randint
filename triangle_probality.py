import random
triangle=0
length=100
for i in range(10000):
    a=random.randint(1,(length-1))
    b=random.randint(1,(length-2))
    while a==b:
        b=random.randint(1,(length-2))
    l1=min(a,b)
    l2=round(abs(a-b))
    l3=length-(l1+l2)
    max_lenght=max(l1,l2,l3)
    if max_lenght<(length-max_lenght):
        triangle=triangle+1
print(triangle/i)
