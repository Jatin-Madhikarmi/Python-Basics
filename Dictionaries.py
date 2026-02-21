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