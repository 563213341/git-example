from car import Car
#--------------------------------------------=--
class Battery():
    def __init__(self,batterysize,model):
        self.size=batterysize
        self.model=model
        
    def showbatterysize(self):
        print('电池容量是：'+str(self.size))

    def getrang(self):
        if self.size==70 and self.model=='tesla':
            rang=240
        elif self.size==80 and self.model=='honda':
            rang=360
        print('这个电池容量版本的续航里程是：'+str(rang))
#---------------------------------------------      
class Elec(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery(80,'honda')

