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
    print(f"The size dimension(shape) of the matrix is {m.shape}")
    print(type(m.shape))
    list1=list(m.shape)
    print(list1[1]) # represents the column of the matrix to determine whether it is odd or even
    if list1[1]/2 != 0:
        sliceVar1=list1[1]-2
        sliceVar2=2
    else:
        sliceVar1=list1[1]/2    
        sliceVar2=list1[1]/2   
    m1=m[:,[0,sliceVar1]]
    m2=m[:,[sliceVar2]]
    return [m1,m2]


m=np.array([[1,2,3],[4,5,6],[7,8,9]])
#m=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(m)
list1=splitMatrix(m)
print(list1[0])
print(list1[1])