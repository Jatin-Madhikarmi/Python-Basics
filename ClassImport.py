class Car:
    def __init__(self,company,model,user):
        print("We have entered the constructor function.\n")
        self.company=company
        self.model=model
        self.user=user
    
    def print_info(self):
        print(f"The car's company is {self.company}")
        print(f"The car's model is {self.model}")
        print(f"The car's owner is {self.user}")

def hello():
    print("\nThis is a hello to the owner of the car.\n")