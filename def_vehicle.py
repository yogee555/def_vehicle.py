# class with vehicle
class vehicle:
    def __init__(self,milage,cost):
        self.milage=milage
        self.cost=cost
    def show_details(self):
        print("I am a vehicle")
        print("milage of vehicle is",self.milage)
        print("cost of vehicle is",self.cost)
v1 = vehicle(500,500)
v1.show_details()