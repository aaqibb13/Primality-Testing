import random
import math
def fermattest(n):
    k=11 #k is a security parameter
    for i in range(0,k-1):
        #The number a is generated randomly in the range 2 -- (n-1)
        a = random.randrange(2,n-1)     
        b = pow(a,n-1,n)
        if b!=1:
            #If a number fails the test, it outputs Composite
            print('Composite',a)
        else:
            print('Probable Prime')
        #The algorithm outputs "Probable Prime" when the algorithm passes
fermattest(237) # Pass the numbers here
