
class Icecream():
    def __init__(self,location,things,flavors):
        self.loc=location
        self.thing=things                        #9.6已完成
        self.fla=flavors
    def icemsg(self):
        print('我喜欢的是产自 '+self.loc+' 这个地方的，有 '+self.thing+' 这种配料的 '+self.fla+' 口味的冰激凌。')
        
mfice=Icecream('无锡','蓝莓','酸奶')
mfice.icemsg()
