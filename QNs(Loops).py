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

def my_odd_even(m):
    m=m.astype(float)
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if m[i,j] % 2 == 0:
                print("Enterd the if block statement")
                print(f"The value of m[i,j] before mofification is {m[i,j]}")
                print(f"The value of np.sin(m[i,j]) is {np.sin(m[i,j])}")
                m[i,j]=np.sin(m[i,j])
                print(f"The value of m[i,j] after mofification is {m[i,j]}")
            else:
                print("Enterd the else block statement")
                print(f"The value of m[i,j] before mofification is {m[i,j]}")
                print(f"The value of np.cos(m[i,j]) is {np.cos(m[i,j])}")
                m[i,j]=np.cos(m[i,j])
                print(f"The value of m[i,j] after mofification is {m[i,j]}")
    return m

#Using numpy function where
def my_odd_even(m):
    m=m.astype(float)
    return np.where(m%2==0 , np.sin(m) , np.cos(m))

m=np.array([[1,2],[3,4]], dtype=float)
print(my_odd_even(m))

def my_mat_mul(m,n):
    a=np.zeros((m.shape[0],n.shape[1]))
    print(f"{m.shape[0]},{m.shape[1]},{n.shape[0]},{n.shape[1]}")
    if (m.shape[1]) == (n.shape[0]):
        for i in range(m.shape[0]):
            for j in range (m.shape[1]):
                for k in range (n.shape[1]):
                    a[i,j]=m[i,j] * n[j,k]
        return a
    else:
        return "Invalid matrices"

m=np.array([[1,2],[4,5]])
n=np.array([[1,2],[4,5]])
print(my_mat_mul(m,n))

def my_saving_plan(p0,i,goal):
    return np.log10(goal/p0) / np.log10(1+i)

print(my_saving_plan(1000,0.05,2000))

M=[0,1,1,1,0]
N=np.array(M)
y=[]
counter=-1
for i in M:
    counter+=1
    if i == 1:
        y.append(counter)
print(y)

words = ['test', 'data', 'analyze']
upperWords=[i.upper() for i in words]
print(upperWords)


def my_connectivity_mat_2_dict(C, names):
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            if C[i,j] == 1:
                print("Hello world")

C = np.array([[0, 1, 0, 1], [1, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 0]])
names = ['Los Angeles', 'New York', 'Miami', 'Dallas']

my_connectivity_mat_2_dict(C,names)