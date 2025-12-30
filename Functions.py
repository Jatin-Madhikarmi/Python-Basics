import numpy as np
print(type(len))
print(type(np.array))

def hello(a):
    return(f"Hello {a}!")

def hello_together(a,b):
    return(f"Hello {a} & {b}!")

name=["John","Amy","Sheldon","Howard","Raj","Jake"]
print(hello(name[0]))
print(hello(name[1]))
print(hello(name[2]))
print(hello(name[3]))
print(hello(name[4]))
print(hello(name[5]))
print(hello_together(name[0],name[1]))

def fullAdder(s1,s0,cin):
    return(s1+s0+cin)

print(fullAdder("1","0","0")) # Concatenation of the string
print(fullAdder(1,0,0)) # Adding the numbers

def adder(a,b):
    print("Inside the adderList function.")
    print(type(a))
    print(type(b))
    return(a+b)

list1=[1,2,3]
list2=[4,5,6]
list3=adder(list1,list2)
print(list3)

tuple1=(1,2,3)
tuple2=(4,5,6)
tuple3=adder(tuple1,tuple2)
print(tuple3)

def airthmethic(a,b):
    return a+b,a-b,a*b,a/b,a**b

x=2
y=4
a,b,c,d,e=airthmethic(x,y)
print(f"{a}")
print(f"{b}")
print(f"{c}")
print(f"{d}")
print(f"{e}")

def setConvert(a):
    print(type(a))
    return set(a)

list1=[1,2,3,4,4,5,]
set1={1,2,2,2,2,4,5,6,7}
print(setConvert(list1))
print(setConvert(set1))

def dataStructure_Additon(a,b):
    return a+b

print(dataStructure_Additon(list1,list2))
print(dataStructure_Additon(tuple1,tuple2))

dict1={"Kathmandu":"Rosebud",
       "Lalitpur":"Rato Bungla"}
dict1["Dhulikhel"]="KU"
dict2={"Bhaktapur":"Genuine"}

def setOperations(a,b):
    return a.union(b), a.intersection(b), a.difference(b), a.issubset(b)

union,intersection,difference,subset=setOperations(set1,set1)
list4=[union,intersection,difference,subset]
for i in list4:
    print(i)



