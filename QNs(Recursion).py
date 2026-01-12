import numpy as np
def my_sum_list(lst):
    counter=0
    for sum in lst:
        counter+=sum

    return counter

list1=[1,12,3,22,1,1]
print(my_sum_list(list1))
print(my_sum_list(range(1,101)))

def my_chebyshev_poly1(n, x):
    def get_tn(n,val):
        if n == 0:
            return 1
        elif n== 1:
            return x
        else:
            return 2 * val * get_tn(n - 1, val) - get_tn(n - 2, val)
        

    y=[get_tn(n,val) for val in x]
    return y

x=[0,1,2,3,4,5]
n=0
print(my_chebyshev_poly1(n,x))


def golden_ratio(n):
    fibs=np.ones(n)

    for i in range(2,n):
        fibs[i]=fibs[i-1] + fibs[i-2]

    return fibs[i].tolist(),fibs[i-1].tolist()

n=10
numerator,denominator=golden_ratio(n+1)
print({numerator/denominator})

def gcd(a,b):
    if b == 0:
        return a
    
    else:
        return gcd(b,a%b)
    
a,b=10,4
print(gcd(a,b))

def my_pascal_row(m):
    n = m - 1
    row = [1] 
    
    current_val = 1
    for k in range(1, n + 1):
        current_val = current_val * (n - k + 1) // k
        row.append(current_val)
        
    return row


row=3
print(my_pascal_row(row)) 



def my_spiral_ones(n):
    # Initialize an n x n matrix of zeros
    matrix = np.zeros((n, n), dtype=int)
    
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    
    while top <= bottom and left <= right:
        # 1. Move Right
        for i in range(left, right + 1):
            matrix[top][i] = 1
        top += 1
        
        # 2. Move Down
        for i in range(top, bottom + 1):
            matrix[i][right] = 1
        right -= 1
        
        # 3. Move Left (Check if top <= bottom still holds)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = 1
            bottom -= 1
            
        # 4. Move Up (Check if left <= right still holds)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = 1
            left += 1
            
    return matrix

n=5
print(my_spiral_ones(5))