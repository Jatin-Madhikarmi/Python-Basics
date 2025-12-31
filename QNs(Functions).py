import numpy as np

def my_sinhx(x):
    y=(np.exp(x)-np.exp(-x))/2
    return y

x,y,z=0,1,2
print(my_sinhx(x))
print(my_sinhx(y))
print(my_sinhx(z))

traingleArea=lambda b,h:(b*h)/2

b,h=2,3
print(f"The area of the traingle where breadth is {b} and height is {h} is {traingleArea(b,h)}")


def splitMatrix(m):
    print(m.shape)


m=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m)
splitMatrix(m)