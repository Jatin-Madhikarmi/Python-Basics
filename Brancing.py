import numpy as np
def my_desired_temp(temp,desired_temp):
    if temp < desired_temp - 5:
        print("Entered the if statement block")
        status="Heat"
    elif temp > desired_temp + 5:
        print("Entered the first elif statement block")
        status="Cold"
    else:
        print("Entered the else statement block")
        status="Off"
    
    return status

temp,desired_temp=65,63
print(my_desired_temp(temp,desired_temp))


x=3
if x>1 and x<2:
    y=1
elif x>2 and x<4:
    y=2
else:
    y=3

a=4
if 1<a<2:
    b=1
elif 2<a<3:
    b=2
elif 3<a<5:
    b=3
else:
    b=4

print(b)
print(y)


def myAdder(a,b,c):

    if not (isinstance(a,(int,float)) \
           or isinstance(b,(int,float)) \
            or isinstance(c,(int,float))):
        raise TypeError("Inputs must be numbers.")
    return a+b+c

a,b,c=1,2,3
print(myAdder(a,b,c))
        
def isOdd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
    
n=1
print(isOdd(n))

def my_circle_cal(r,cal):

    if cal == "area":
        return np.pi*r**2
    elif cal == "circumference":
        return 2*np.pi*r
    else:
        return "No appropriate operation was found"
    
r,cal=2,"Area"
print(my_circle_cal(r,cal.lower()))

isStudent=False
if isStudent:
    person="Student"
else:
    person="Not Student"

print(person)

man="Student" if isStudent else "Not Student"
print(man)