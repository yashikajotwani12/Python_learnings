class Train:
    def __init__(self, name, fare, seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getfareinfo(self):
        print(f"the name of the train is {self.name}")
        print(f"the fare of the train is {self.fare}")
        print(f"the seats of the train is {self.seats}")

    def booktickets(self):
        if(self.seats>0):
            print(f"Your ticket has been booked !! your seat no. is {self.seats}")
            self.seats=self.seats-1
        else:
            print(f"sorry!! train is full")
        
intercity=Train("IntercityExpress",90,1)
intercity.getfareinfo()
intercity.booktickets()
intercity.getfareinfo()
intercity.booktickets()
intercity.getfareinfo()

