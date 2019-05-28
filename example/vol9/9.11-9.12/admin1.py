
class Us():
    def __init__(self,firstname,lastname,userage,usercountry):
        self.fn=firstname
        self.ln=lastname
        self.ua=userage
        self.uc=usercountry
        self.login_attempts=0

    def du(self):
        print(self.fn+' '+self.ln+' 是一个 '+str(self.ua)+' 岁的 '+self.uc+' 人')

    def gu(self):
        print('欢迎你 '+self.fn+' '+self.ln)

    def la(self):
        print('登录次数是：'+str(self.login_attempts))

    def inla(self):
        self.login_attempts +=1
        
    def rela(self):
        self.login_attempts =0              






