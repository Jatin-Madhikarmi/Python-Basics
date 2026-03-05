class Car:
    def __init__(self,model,owner,company):
        self.model=model
        self.owner=owner
        self.company=company

def my_func():
    model="Ns-200"
    owner="Jack"
    company="Pulsar"
    return Car(model,owner,company)

car=my_func()
my_list=list()
my_list.append(car.__dict__)
print(len(my_list))
print(my_list)