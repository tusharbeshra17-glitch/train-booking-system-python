import random
class Train :
    def __init__(self,train_No,fro,to) :
        self.train_No=train_No
        self.fro=fro
        self.to=to
        
    def Book(self) :
        print(f"ticket no {self.train_No} is booked from {self.fro} to {self.to}")
    
    def get_status(self) : 
        print(f"train no {self.train_No} is on the time ")    
    
    def get_fare(self) :
        print(f"ticket no {self.train_No} which is from {self.fro} to {self.to} is  Rs {random.randint(500,2000)}")
    
    def get_info(self) :
        self.Book()
        self.get_status()
        self.get_fare()
t1=Train(random.randint(1111,9999),"cuttack","jammu")
t1.get_info()
