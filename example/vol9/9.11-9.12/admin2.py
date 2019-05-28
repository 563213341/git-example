from admin1 import Us
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
