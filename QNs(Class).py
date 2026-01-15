import numpy as np
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def print_points(self):
        print(f"The inputted points are {self.x} and {self.y}")

    def calculate_distance(self,x,y):
        xnew=np.power(self.x - x,2)
        ynew=np.power(self.y - y,2)
        print(f"The distance is {np.sqrt(xnew+ynew)}")

p1=Point(1,2)
p1.print_points()
p1.calculate_distance(0,0)

class ComplexNumbers():
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

    def addition(self,r,i):
        realNew=self.real + r
        imaginaryNew=self.imaginary + i
        print(f"The summed imaginary number is {realNew} + {imaginaryNew}i")

    def complement(self):
        sign=-self.imaginary
        if sign < 0:
            signValue="-"
        else:
            signValue="+"
        print(f"The complement of the number is {-self.real} {signValue} {self.imaginary}i")

    def print_values(self):
        print(f"{self.real} + {self.imaginary}i")

CN1=ComplexNumbers(1,2)
CN1.print_values()
CN1.complement()
CN1.addition(3,4)
CN1.print_values()
        