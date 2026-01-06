import numpy as np
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
    
print(factorial(5))

def fibonnaci_recursion(n):
    if n== 1:
        out=1
        print(out)
        return out
    elif n== 2:
        out =1
        print(out)
        return out
    else:
        out=fibonnaci_recursion(n-1)+fibonnaci_recursion(n-2)
        print(out)
        return out
    
print(fibonnaci_recursion(5))

def fibonacci_iterative(n):
    fibs=np.ones(n)

    for i in range(2,n):
        fibs[i]=fibs[i-1] + fibs[i-2]

    return fibs

print(fibonacci_iterative(5))