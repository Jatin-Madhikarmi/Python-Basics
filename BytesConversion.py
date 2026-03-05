byte_number=b'\x00\x10'

int_number=int.from_bytes(byte_number,"big",signed=True)

print(f"The byte number is {byte_number}")
print(f"The int number is {int_number}")

number=12
byte_number=format(number,'b')
print(byte_number)