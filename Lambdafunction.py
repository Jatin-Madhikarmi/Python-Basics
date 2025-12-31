square=lambda x:x**2 # one liner function

def square(x):
    return x**3 
# here two functions have the same name inside of throwing ambiguity error the last fucntion defined with the name is the one selected

a,b=2,5
print(square(a))
print(square(b))

my_adder=lambda x,y,z:x+y+z

x,y,z=1,2,3
print(my_adder(x,y,z))



