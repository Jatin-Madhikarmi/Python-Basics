with open('hello.txt','r') as f:
    data=f.read()

print(data)
print(str(data))
print(str(len(data)))
print(b'str(len(data))')
print(str(len(data)).encode())