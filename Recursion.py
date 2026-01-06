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


def hanaoiTowers(n,fromTower,toTower,altTower):

    if n!=0:
        hanaoiTowers(n-1,fromTower,altTower,toTower)

        print(f"BLock {n} is moved from tower {fromTower}  to tower {toTower}")

        hanaoiTowers(n-1,altTower,toTower,fromTower)

print(hanaoiTowers(3,1,3,2))


def my_QuickSort(lst):
    if len(lst)  <= 1:
        sortedList=lst
    else:
        pivot=lst[0]

        bigger=[]
        smaller=[]
        same=[]

        for i in lst:
            if i > pivot:
                bigger.append(i)
            elif i < pivot:
                smaller.append(i)
            else:
                same.append(i)
    
        sortedList=my_QuickSort(smaller) + same + my_QuickSort(bigger)
    
    return sortedList

list1=[62,3,2,3421,23,1,21,441,5]
print(my_QuickSort(list1))