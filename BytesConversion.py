byte_number=b'\x00\x10'

int_number=int.from_bytes(byte_number,"big",signed=True)

print(f"The byte number is {byte_number}")
print(f"The int number is {int_number}")

number=12
byte_number=format(number,'b')
print(byte_number)

sha='04c3f44424e60ba98e3a3f13d3d70ccab9b23592'
int_sha=int(sha,16)
byte_sha=int_sha.to_bytes(20,"big")
from_byte_to_int_sha=int.from_bytes(byte_sha,"big")
print(sha)
print(int_sha)
print(byte_sha)
print(from_byte_to_int_sha)