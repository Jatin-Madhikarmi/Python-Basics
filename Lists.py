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

nFactor=8
list_7=[12]*nFactor # This is called list multiplication and when [] term is multiplied with any number(n) then the list is repeated n times
                    #with the number inside [] 
print(list_7)

list_8=[0,*list_7,4] # Unpacking list operator is *
print(list_8)

list_9=[3]
print("The value of the list_9 after slicing is :\n")
print(list_9[:-1])


memory=[1,2,3]
least_used=1
least_used_index=memory.index(least_used)
new_element=0
print(f"The least used element is {least_used} and it's index is {least_used_index}")
memory[least_used_index]=new_element
print(f"After rep the memory becomes {memory}")
print(memory)

page_reference_string=[1,2,3,1,5,6,7,8,9]
index=5
visited=[]
for i in page_reference_string[0:index]:
    visited.append(i)
    print(i)
print(visited)

visited=[]
memory=[1,2,3]
for i in page_reference_string[0:index]:
    if i in memory:
        if i not in visited:
            visited.append(i)

print(visited)

string=[1,2,2,3,4,3,2,1,2,4,6]
memory=[4,2,1]
index=5
visited=[]
print("HERE WE GO")
for i in string[index:]:
    if i in memory:
        if i not in visited:
            visited.append(i)
print(visited)