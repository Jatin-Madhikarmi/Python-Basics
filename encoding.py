with open('hello.txt','r') as f:
    data=f.read()

print(data)
print(str(data))
print(str(len(data)))
print(b'str(len(data))')
print(str(len(data)).encode())

def set_value(val):
    temp=val
n=5
value=set_value(n)
print(value)
