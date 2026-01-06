def my_sum_list(lst):
    counter=0
    for sum in lst:
        counter+=sum

    return counter

list1=[1,12,3,22,1,1]
print(my_sum_list(list1))
print(my_sum_list(range(1,101)))

def my_chebyshev_poly1(n,x):
    if n == 0:
        return [1]*x.lenght()
    
    elif n == 1:
        return x
    
    else:
        return 2*my_chebyshev_poly1()
x=[0,1,2,3,4,5]
n=0
print(my_chebyshev_poly1(n,x))

