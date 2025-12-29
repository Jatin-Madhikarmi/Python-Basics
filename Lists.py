#Mutuable data structures
list_1=[1,2,3]
list_2=["hello","world","mom"]

print(list_1)
print(list_2)
print(list_1 + list_2)

list_3=list_1+list_2
print(list_3)

list_1.append(4)
list_4=[list_1,list_2,list_3]
print(list_4[0])

list_1.insert(4,'father')
print(list_1)

list_5=[]
print(list_5)
list_5.append(5)
print(list_5)
list_5.insert(5,"10")
print(list_5)

if "10" in list_5:
    print("true")
else:
    print("false")

list_6=list("hello    world")
print(list_6)
print(list_6.count("h"))

list_0=[list_4[0]]
print(list_0)