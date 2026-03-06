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
my_list.append(car)
first_entry_list=my_list[0]
print(f"The list is {my_list}")
print(f"The model is {first_entry_list.model}")
print(f"The owner is {first_entry_list.owner}")
print(f"The compnay is {first_entry_list.company}")