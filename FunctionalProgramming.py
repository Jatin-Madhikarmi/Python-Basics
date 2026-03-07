my_list=[1,2,3,4,5]

squared_list=[x**2 for x in my_list if x%2==0]
print(squared_list)

squared_list=map(lambda x:x**2,filter(lambda x: x%2 ==0,my_list))
sq_list=list()
for item in squared_list:
    sq_list.append(item)

print(sq_list)