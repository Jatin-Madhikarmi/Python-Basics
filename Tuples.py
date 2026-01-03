#Immutable data structures
tuples_1=(1,2,3)
print(tuples_1)

tuples_2=("hello","world","mom")
print(tuples_2)

print(tuples_1 + tuples_2)

tuples_3=tuples_1 + tuples_2
print(tuples_3)

print(tuples_3.count(1))

# tuples_1[0]=0 can't change the tuple 

list_1=[("apple,1"),("orange,3"),("watermeleon,5")]
print(list_1[0])
print(type(list_1))

tuples_4=("apple,1","orangle,3","watermelon,5")
print(tuples_4[0])
print(type(tuples_4))

tuples_5=()
tuples_5=6,7
print(tuples_5)

list_2=[]
# list_2=7
list_2.append(6)
list_2.append(9)
print(list_2)

scaleFactor=3
tuples_6=("Python",)*scaleFactor
print(tuples_6)