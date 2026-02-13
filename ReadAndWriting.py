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

#JSON Files
import json
Uni={
    "Name":"Kathmandu University",
    "Location":{
        "Country":"Nepal",
        "District":"Kavre"
    },
    "Status":"Open",
    "list1":[
        "Student 1,"
        "Student 2,"
        "Student 3,"
    ]
}

json.dump(Uni,open('School.json','w'))

jsonFile=json.load(open('./School.json','r'))
print(jsonFile)
print(type(jsonFile))

#HDF5 (Heirachical Data Format)
import h5py
acc_1=np.random.random(100)
start_time_1=24354231
operating_time_1=4.00
location_1="Kathmandu"

acc_2=np.random.random(100)
start_time_2=2345324234
operating_time_2=1.00
location_2="Bhaktapur"

hf=h5py.File('station.hdf5','w')


hf['/acc1/1/data']=acc_1
hf['/acc1/1/data'].attrs['start_time']=start_time_1
hf['/acc1/1/data'].attrs['operating_time']=operating_time_1
hf['/acc1/1/data'].attrs['location']=location_1

hf['/acc/2/data']=acc_2
hf['/acc/2/data'].attrs['start_time']=start_time_2
hf['/acc/2/data'].attrs['operating']=operating_time_2
hf['/acc/2/data'].attrs['location']=location_2

hf['/gps/1/data']=np.random.random(100)
hf['/gps/1/data'].attrs['start_time']=2.00
hf['/gps/1/data'].attrs['operatin_time']=23456234
hf['/gps/1/data'].attrs['location']="Lalitpur"

hf.close()

hf_in=h5py.File('./station.hdf5','r')

print(hf_in.keys())
acc=hf_in['acc']
print(acc.keys())
info=hf_in['acc/2/data']
print(info[:10])
print(list(info.attrs))
print(info.attrs['location'])
print(info.attrs['operating'])
print(info.attrs['start_time'])


print(hf_in.keys())
gps=hf_in["gps"]
print(gps.keys())
data_stored=hf_in['/gps/1/data']
print(data_stored[:10])
print(list(data_stored.attrs))
print(data_stored.attrs['location'])
print(data_stored.attrs['operatin_time'])
print(data_stored.attrs['start_time'])
