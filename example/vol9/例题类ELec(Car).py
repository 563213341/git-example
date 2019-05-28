class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.rec=8000

    def getm(self):
        print(str(self.year)+' '+self.make+' '+self.model)      
         
    def record(self):
        print('这辆车的里程是'+str(self.rec))

    def uprecord(self,mile):
        if mile>=self.rec:
            self.rec=mile
        else:
            print('不准调表')
            
    def riserecord(self,mile):
        if mile>=0 :
            self.rec +=mile
        else:
            print('不准输入负值')
#---------------------------------------------
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
#--------------------------------------------=--
mytesla=Elec('tesla','model3',2016)
mytesla.getm()
mytesla.battery.showbatterysize()
mytesla.battery.getrang()
