class Dog:
    name= None
    color= None
    def __init__(self, name):
        print("i will be printed without calling")
        self.name= name
dog1=Dog("Aslan")
print(dog1.name)

dog2=Dog("Harley")
print(dog2.name)
