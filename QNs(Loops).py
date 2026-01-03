import numpy as np
y=0
for i in range(1000):
    for j in range(1000):
        if i==j:
            y+=1
print(y)

def my_n_max(x,n):
    greatest=[]
    counter=0
    for i in x:
        greatest.append(max(x))
        x.remove(max(x))
        counter+=1
        if counter == n:
            break
    return greatest

x=[1,2,3,4,5,6,7,8,9,10]
n=3
print(my_n_max(x,n))