uncompressed_list=[2,3,4,5,2,1,3,5,7]

def delta_compression(uncompressed_list):
    compressed_list=[]
    prev_value=0
    for i in uncompressed_list:
        compressed_list.append(i-prev_value)
        prev_value=i

    return compressed_list

print(f"The uncompressed list is {uncompressed_list}")
compressed_list=delta_compression(uncompressed_list)
print(f"The compressed list is {compressed_list}")
        

