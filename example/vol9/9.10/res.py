class Rest():
    
    def __init__(self,res_name,cui_type):
        self.name=res_name
        self.type=cui_type

    def des_res(self):
        print(self.name+'是一家正在营业的 '+self.type+'口味餐厅')

    def op_res(self):
        print(self.name+'欢迎你的光临')



