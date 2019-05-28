
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
        self.login_attempts =0              #9.7已完成  9.8已完成
#----------------------------------------------------------------------------
class Pri():
    def __init__(self,pri=['can add post','can del post']):
         self.pri=pri
    def showpri(self):
        print('管理员的权限是'+self.pri[0]+'和'+self.pri[1])
#--------------------------------------------------------------------------
class Admin(Us):
    def __init__(self,firstname,lastname,userage,usercountry):
        super().__init__(firstname,lastname,userage,usercountry)
        self.pri=Pri()

biguser=Admin('朱','仪',32,'中国')
print(biguser.fn+' '+biguser.ln+' 欢迎你')        
biguser.pri.showpri()


