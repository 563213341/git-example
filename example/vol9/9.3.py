'''
class Us():
    def __init__(self,firstname,lastname,userage,usercountry):
        self.fn=firstname
        self.ln=lastname
        self.ua=userage
        self.uc=usercountry

    def du(self):
        print(self.fn+' '+self.ln+' 是一个 '+str(self.ua)+' 岁的 '+self.uc+' 人')

    def gu(self):
        print('欢迎你 '+self.fn+' '+self.ln)

biguser=Us('朱','仪',32,'中国')
print(biguser.fn+' '+biguser.ln+' 欢迎你')      #9.3已完成

biguser.du()
biguser.gu()'''
