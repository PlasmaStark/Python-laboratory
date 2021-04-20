# modified & fixed version

from math import gcd
import random

def Fermat():
    n = int(input("-> insert wannabe-prime n: ")) 
    k = int(input("-> insert iterations: ")) 
    if n==2: 
        return True
    
    correct = (n>3) & (n%2 != 0)
    if correct:
        for i in range(k):
            while True:
                r = random.randint(1,n-1)
                if gcd(r,n)==1:
                    break
            if pow(r, n-1, n) != 1:
                correct = False
                break
    
    print(str(n) + " is probable prime: " + str(correct))
    print("ended at iteration " + str(i+1))
    return correct
