uncompressed_list=[2,3,4,5,2,1,3,5,7]

def delta_compression(uncompressed_list):
    compressed_list=[]
    prev_value=0
    for i in uncompressed_list:
        compressed_list.append(i-prev_value)
        prev_value=i

    return compressed_list

def delta_decompresseion(compressed_list):
    uncompressed_list=[]
    curr_value=compressed_list[0]
    prev_value=0
    for i in compressed_list:
        curr_value=i+prev_value
        uncompressed_list.append(curr_value)
        prev_value=curr_value

    return uncompressed_list

print(f"The uncompressed list is {uncompressed_list}")
compressed_list=delta_compression(uncompressed_list)
print(f"The compressed list is {compressed_list}")
new_uncompressed_list=delta_decompresseion(compressed_list)
print(f"The new uncompressed list is {new_uncompressed_list}")

