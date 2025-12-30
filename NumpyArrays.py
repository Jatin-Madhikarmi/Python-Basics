import numpy as np
x=np.array([1,2,3])
print(x)
print(f"The first element of the matrix x is {x[0]}")
print(f"The last element of the matrix x is {x[-1]}")

y=np.array([[1,2,3],[4,5,6]])
print(y)
print(y.shape) #prints the dimension of the matrix
print(y.size) #prints the no of elements in the matrix

z=np.arange(0,200,5)
print(z)
print(type(z))

print(np.arange(0.5,3,0.5))

print(np.linspace(3,9,5))


a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[:,[0,1,2]])

b=np.identity(3)
print(b)

c=np.empty(3)
print(c)

d=np.arange(1,7)
print(f"Before indexing is {d}")
d[0:3]=7
print(f"After indexing is {d}")

e=np.zeros((2,2))
print(f"Before the array indexing {e}")
e[0,0]=1
e[0,1]=2
e[1,0]=3
e[1,1]=4
print(f"After the array indexing {e}")

print(e**2) # exponential i.e power raised to 2

f=np.array([[1,2],[3,4]])
print(e+f)
print(np.sqrt(f))
print(f>=3)
g=f[f>1]
print(g)
g[g>3]=3
print(g)
print(f.T)