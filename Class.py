import numpy as np
class Person():
    def __init__(self,name,age):
        self.name =name
        self.age=age
        
    def Greetings(self):
        print(f"Hello my name is {self.name} an I am {self.age} years old.")

Person1=Person("Jonathon","30")
Person2=Person("Nancy","30")
Person1.Greetings()
Person2.Greetings()

print(Person2.name,Person2.age)

class Student():
    n_instances=0
    def __init__(self,sid,name,gender):
        self.name=name
        self.sid=sid
        self.gender=gender
        self.type="Learning"
        Student.n_instances+=1

    def say_name(self):
        print(f"My name is {self.name} and I am {self.type}")

    def report(self,score):
        self.say_name()
        print(f"My student ID is {self.sid}")
        print(F"My score is {score}")

    def num_instances(self):
        print(f'We have {Student.n_instances}-instance in total')

Student1=Student("1","John","M")
Student1.num_instances()
Student1.say_name()
Student2=Student("2","David","M")
Student1.num_instances()
Student2.num_instances()
Student1.report(100)


class Sensor():
    def __init__(self,name,location,record_date):
        self.name=name
        self.location=location
        self.record_date=record_date
        self.data={}

    def add_data(self,t,data):
        self.data["time"]=t
        self.data["data"]=data
        print(f"We have {len(data)} points stored")
    
    def clear_data(self):
        self.data={}
        print(f"The Dictionary is cleared ")

Sensor1=Sensor("DavidPutra","Jelloa Do","2025")
data = np.random.randint(-10, 10, 10)
print(data)
Sensor1.add_data(np.arange(10),data)
Sensor1.clear_data()


class Accelerometer(Sensor):
    def show_type(self):
        print("I am an accelerometer.")

Accelerometer1=Accelerometer("acc1","Okland","2026")
Accelerometer1.show_type()
data=np.random.randint(-10,10,5)
Accelerometer1.add_data(np.arange(10),data)
Accelerometer1.clear_data()

class UBCacc(Accelerometer):
    def show_type(self):
        print(f"I am and accelerometer with the type {self.name}")

UBC1=UBCacc("UBC","Berkley","2026")
UBC1.show_type()

class NewSensor(Sensor):
    def __init__(self, name, location, record_date,brand):
        super().__init__(name,location,record_date)
        self.brand=brand
        

NewSensor1=NewSensor("S1","Utah","2025-01-01","ABC")
print(NewSensor1.brand)
print(NewSensor1.name)

class Employee():
    def __init__(self,name,id,location):
        self.name=name
        self._id=id
        self._location=location
        self.__department="Management"

    def get_department(self):
        print(f"The department is {self.__department}")

    def __set_department(self,department):
        self.__department=department

E1=Employee("John","001","Bamel")
E1.get_department()
E1.set_department("CEO")
E1.get_department()
print(E1.name)
print(E1._id)
print(E1.__department)
        
    