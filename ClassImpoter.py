class Car:
    def __init__(self,model,name,user):
        self.model=model
        self.name=name
        self.user=user
        self.print_info()
    
    def print_info(self):
        raise Exception(f"Not a clas function call")