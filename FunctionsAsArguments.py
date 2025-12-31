import numpy as np
f=max
print(type(max))
print(type(f))

print(f([1,2,5]))
print(max([1,2,5]))

def func_plus_1(f,x):
    return (f(x) + 1)


x,y=5,2
print(func_plus_1(np.sin,np.pi/2))
print(func_plus_1(np.cos,np.pi/2))
print(func_plus_1(np.sin,np.pi))
print(func_plus_1(np.cos,np.pi))
print(func_plus_1(lambda x:x+2,2))
print(func_plus_1(lambda x:x**2,3))