import numpy as np
file=open('test.txt','w')


for i in range(5):
    file.write(f"This is line {i}\n")

file.close()

file=open('./test.txt','r')
contents=file.readline()
file.close()
print(contents)

my_arr=np.array([[1,2,3],[4,5,6]])
np.savetxt('./my_array.txt',my_arr,fmt='%.2f',header='Col1 Col2 Col3')


file=open('./my_array.txt','r')
reterived_array=file.read()
file.close()
print(reterived_array)

print(np.loadtxt('./my_array.txt'))