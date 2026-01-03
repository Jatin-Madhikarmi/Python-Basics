import numpy as np
def my_tip_bill(bill,party):
    if party <6:
        return bill*(0.15)
    elif party < 8:
        return bill*(0.18)
    elif party < 11:
        return bill*(0.2)
    else:
        return bill*(0.25)
    
bill,party=109.29,12
print(f"The required tip is {my_tip_bill(bill,party)}")

def my_mult_operation(a,b,operation):

    if operation == "add":
        return a+b
    elif operation == "subtract":
        return a-b
    elif operation == "mul":
        return a*b
    elif operation == "div":
        return a/b
    elif operation == "pow":
        return a**b
    else:
        return "The operation was not found"
    
x,y=np.array([1,2,3,4]),np.array([2.,3,4,5])
operation="add"
print(my_mult_operation(x,y,operation.lower()))

def my_make_size10(x):
    x_list = list(x)
    
    if len(x_list) >= 10:
        result = x_list[:10]
    else:
        result = x_list + [0] * (10 - len(x_list))
    
    # Convert back to a clean NumPy array at the very end
    return np.array(result)

    
x=np.arange(1,3,1)
print(my_make_size10(x))

def my_alaram(s1,s2,s3):
    if np.abs(s1-s2) > 10  or np.abs(s1-s3) > 10 or np.abs(s2-s3) > 10:
        return "Alaram"
    else:
        return "Safe"
    
s1,s2,s3=98,98,99
print(my_alaram(s1,s2,s3))


def my_n_roots(a,b,c):
    r1=(-b + (b**2 - 4*a*c)**0.5)/2*a
    r2=(-b - (b**2 - 4*a*c)**0.5)/2*a
    set1={r1,r2}
    if (b**2 >= 4*a*c):
        if r1 == r2:
            n_roots=1
        else:
            n_roots=2
    else:
        n_roots=2
    return set1,n_roots

a,b,c=3,4,5
print(my_n_roots(a,b,c))
         