'''You have a stick of arbitrary length. You break the stick uniformly at random along it’s length at two places, leaving you with three distinct pieces.
What is the probability that you can form a triangle with the resulting three pieces?'''

import random
triangle=0                              #For storing values of favourable cases
length=100                              #Lenght of stick.Length doesnot changes the probality,So any value can be assigned
for i in range(10000):                  #We are doing this experiment 10000 times
    a=random.randint(1,(length-1))      #First point on stick
    b=random.randint(1,(length-2))      #Second point on stick
    while a==b:                         #Ensuring that both points are not the same point
        b=random.randint(1,(length-2))
    l1=min(a,b)                         #Length 1,It is the shortest length among first 2
    l2=round(abs(a-b))                  #Length 2,It is the next lenght among two randomly selected points
    l3=length-(l1+l2)                   #Length 3
    max_lenght=max(l1,l2,l3)            #Calculating max lenght among three sides
    if max_lenght<(length-max_lenght):  #Checking if three sides satifies triangle inequality
        triangle=triangle+1             #Counting the favourable cases
print(triangle/i)                       #Finally the probality(favourablecases/total experiments)
