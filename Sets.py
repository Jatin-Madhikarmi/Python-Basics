list_1=[1,1,1,12,3,4,3,2,1]
set_1=set(list_1)
print(set_1)
print(type(set_1))

tuples_1=(1,1,1,2,3,4,5,5,3,2,1)
set_2=set(tuples_1)
print(set_2)
print(type(set_2))

set_3={"banana","apple","watermelon"}
print(set_3)
print(type(set_3))

set_4={1,1,1,45,6,7,1,8,9,0,6,5,4,12,2,3}
print(set_4)
print(set_1.issubset(set_4))
print(type(set_4))
print(set_4.union(set_1))
print(set_4.intersection(set_1))


set_5={"hello","world","mom"}
print(set_5.union(set_3))
print(set_5.intersection(set_3))

