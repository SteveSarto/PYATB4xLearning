#Encapulation

class Car:
    name= None
    password= 123

    def __init__(self):
        print("sdjfiw")
    def change_Pass(self):
        self.password="pramod"

car_obj= Car()
print(car_obj.password)
car_obj.change_Pass()
