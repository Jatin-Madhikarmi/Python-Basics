dict_1={"apple":3,
        "bannana":4,
        "watermelon":5}

print(dict_1["watermelon"])
print(dict_1.keys())
print(dict_1.values())
print(dict_1.__len__())
print(type(dict_1))

tuples_1={}
tuples_1=6,7
print(type(tuples_1))

dict_2={}
dict_2["Kathamndu"]="Rosebud","GEMS"
print(dict_2["Kathamndu"])
print(dict_2)
dict_2["Dhulikhel"]="KU"
print(dict_2.keys())
print(dict_2.values())

dict_3=dict([("Bhaktapur","Genuine"),("Lalitpur","St. Xaviers")])
print(dict_3)


if "Genuine" in dict_3: # works only for the key
    print("True")
else:
    print("False")

if "Genuine" not in dict_3: 
    print("True")
else:
    print("False")

list_1=list(dict_3) # works only for the key
print(list_1)

list_2=[(1,"Door1"),(2,"Door2"),(3,"Door3")]
dict_4=dict(list_2)
print(dict_4[2])
print(dict_4.keys())
print(dict_4.values())

dict_5=dict_1 | dict_2 # Merging operator is |
print(dict_5)

dict_6={**dict_5,"apple":"pen"} # Unpacking the dictionary operator is **dict_name
print(dict_6)


print("New disctionaries")
dict7={"key":"Kathamndu"}
value="Bhaktapur"
dict7["key"]=value
print(dict7)

dict7.pop("key")
print(dict7)

new_dict=dict()
key="Nepal"
#new_dict["Nepal"]=["Bhaktapur","Dharan"]
if key in new_dict:
    if (type(new_dict[key])) == list:
        new_dict[key].append("Kathmandu")
    else:
        new_dict[key]=[new_dict[key],"Lalitpur"]
else:
    new_dict[key]="Birtanagar"
print(new_dict)

new_dict=dict()
for i in range(5):
    new_dict[i]=i+1

print(new_dict)
new_dict.pop(0)
print(new_dict)

new_dict.clear()
for i in range(5):
    if len(new_dict.keys()) !=3:
        new_dict[i]=i+1
    else:
        pass
print(new_dict)

list1=[1]
new_dict.pop(list1[-1])
print(new_dict)

page=1
least_dict=dict()
for i in new_dict.keys():
    # Find the key with the least value
    if len(least_dict.keys()) == 0:
        least_dict[i]=new_dict[i]
        old_data=least_dict[i]
    else:
        new_data=new_dict[i]
        if new_data < old_data:
            print(f"The new data {new_data} is smaller than old data {old_data}")
        else:
            print(f"The new data {new_data} is  NOT smaller than old data {old_data}")

    pass

print(least_dict)



