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

data = np.random.random((100,5))
np.savetxt('test.csv',data,delimiter=',',fmt='%.2f',header='c1, c2, c3, c4, c5')

file=open('./test.csv','r')
contents=file.read()
file.close()
print(contents)

#Pickle Files
import pickle 
dict1={'A':0,
       'B':1,
       'C':'2'}

pickle.dump(dict1,open('testPickle.pkl','wb'))

my_dict=pickle.load(open('./testPickle.pkl','rb'))
print(my_dict)

infilne=open('./testPickle.pkl','rb')
our_dict=pickle.load(infilne,encoding="latin1")
print(our_dict)
infilne.close()