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


car=Car('honda','civic',2016)

car.getm()
car.uprecord(10000)
car.record()

car.riserecord(-200)
car.record()
