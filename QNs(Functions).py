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

#My implementation
def splitMatrix(m):
    print(f"The size dimension(shape) of the matrix is {m.shape}")
    print(type(m.shape))
    list1=list(m.shape)
    print(list1[1]) # represents the column of the matrix to determine whether it is odd or even
    print(type(list1[1]))
    print(f"The value of the column is {list1[1]}")
    slicer=list1[1]
    if slicer%2 == 0:
        print(f"The number is divisible by 2")
        print("Entered the if  statement block")
        sliceVar1=list1[1]//2 - 1  
        sliceVar2=list1[1]//2 
        sliceVar3=list1[1]-1
        print(f"The value of sliceVar1 is {sliceVar1}")
        print(type(sliceVar2))
        print(f"The value of sliceVar2 is {sliceVar2}")
        m1=m[:,[0,sliceVar1]]
        m2=m[:,[sliceVar2,sliceVar3]]
    else:
        print(f"The number is not divisible by 2")
        print("Entered the else statement block")
        sliceVar=[]
        for i in range(list1[1]-1):
            sliceVar.append(i)

        for i in range(list1[1]//2 + 1 ):
            print(f"First for loop {i}")
            m1=m[:,[0,sliceVar[i]]]
    

        i=list1[1]//2 + 1
        for i in range(list1[1]-1):
            print(f"Second for loop {i}")
            m2=m[:,[sliceVar[i]]]
                
    
    return [m1,m2]

#Google Gemini Implementation 
def splitMatrix(m):
    cols=m.shape[1] # get the no of columns in the matrix
    mid=(cols+1)//2

    m1=m[:,:mid]
    m2=m[:,mid:]
    return [m1,m2]


m=np.array([[1,2,3],[4,5,6],[7,8,9]])
#m=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
m=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
print(m)
list1=splitMatrix(m)
print(list1[0])
print(list1[1])