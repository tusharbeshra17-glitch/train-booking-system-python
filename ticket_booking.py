import random
import datetime
class Train :
    def __init__(self,train_No,fro,to,passenger) :
        self.train_No=train_No
        self.fro=fro
        self.to=to
        self.passenger=passenger
        self.fare=None
        self.seat_no=None
        self.booking_time=None

        
    def get_date(self) :
        self.booking_time=datetime.datetime.now().strftime("%d/%m/%y,%H:%M:%S")

    def Book(self) :
        self.seat_no = random.randint(1, 100)
        print(f"ticket no {self.train_No} is booked from {self.fro} to {self.to}")
    
    def get_status(self) : 
        print(f"train no {self.train_No} is on time ")    
    
    def get_fare(self) :
        self.fare=random.randint(500,2000)
        print(f"Ticket no {self.train_No} which is from {self.fro} to {self.to} is  Rs {self.fare}")
    
    def get_info(self) :
        self.Book()
        self.get_status()
        self.get_fare()
        self.get_date()

    def print_ticket(self) :
        print("\n===== TRAIN TICKET =====")
        print(f"Passenger : {self.passenger}")
        print(f"Train No  : {self.train_No}")
        print(f"Seat No   : {self.seat_no}")
        print(f"From      : {self.fro}")
        print(f"To        : {self.to}")
        print(f"Fare      : Rs {self.fare}")
        print(f"Booked On : {self.booking_time}")
        print("="*40)


starting_point=input("Enter starting station:")
end_point=input("Enter destination station:")
name=input("enter name of passenger :")
t1=Train(random.randint(1111,9999),starting_point,end_point,name)
t1.get_info()
t1.print_ticket()