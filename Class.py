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