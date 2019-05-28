class Dog():

    def __init__(self,name,age):
        self.dog_name=name
        self.dog_age=age
        
    def sit(self):
        print(self.dog_name.title() + " is now sitting.")
        
    def roll_over(self):
        print(self.dog_name.title() + " rolled over!")
        


my_dog=Dog('willn',26)


print('狗名:'+my_dog.dog_name.title())
print('狗龄:'+str(my_dog.dog_age))

my_dog.sit()
my_dog.roll_over()
