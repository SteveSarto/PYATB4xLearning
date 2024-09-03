class Person:

    def __init__(self):
        self.name=input("enter your name")
        self.age=input("enter your age")
        self.phno=input("enter your phno")
        self.occupation=input("enter your occupation")

    def display(self):
        print(f"Name is {self.name}")
        print(f"age is {self.age}")
        print(f"phno is {self.phno}")
        print(f"Occupation is {self.occupation}")
person1=Person()
person1.display()
