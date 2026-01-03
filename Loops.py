import numpy as np
n=0
for i in range(1,4):
    n=n+i

print(n)

for c in "watermelon":
    print(c)

s="apple"
for i in range(len(s)):
    print(s[i])

x=0
y=[2,3,1,3,3]

for i in y:
    x+=i

print(x)

dict1={"One":1,
       "Two":2,
       "Three":3}

for key in dict1.keys():
    print(key,dict1[key])

for key,value in dict1.items():
    print(key,value)

a=["One","Two","Three"]
b=[1,2,3]

for i,j in zip(a,b):
    print(i,j)

def haveDigits(s):
    out=0

    for c in s:
        if c.isdigit():
            out=1
            break;
    return out

print(haveDigits("Only for you"))

for i in range(5):
    if i==2:
        continue
    print(i)

x=np.array([[1,2],[3,4]])
m,n=x.shape
s=0
for i in range(n):
    for j in range(m):
        s+=x[i,j]

print(s)

n,i=8,0

while n>=1:
    n/=2
    i+=1
print(i)

x=range(5)
y=[]

for i in x:
    y.append(i**2)

print(y)

y=[i**2 for i in x if i%2==0]
print(y)

y=[]
for i in range(5):
    for j in range(2):
        y.append(i+j)
    
print(y)

y=[i+j for i in range(5) for j in range(2)]
print(y)

x={"a":1,
   "b":2,
   "c":3}

cubed={key:v**3 for (key,v) in x.items()}
print(cubed)

set1={1,2,3,4,5,6}
set2=[i**2 for i in set1]
print(type(set2))
print(set2)
