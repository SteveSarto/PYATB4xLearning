class Employee:
    name=None
    age= None
    phone= None
    address=None
    eid=None

    def __init__(self,name,age,phone,address,eid):
        print("Employee details are")
        self.name=name
        self.age=age
        self.phone=phone
        self.address=address
        self.eid=eid
    def walk(self):
        print("i can walk")
    def talk(self):
        print("i can Talk")
n1=input("enter name for employee 1")
a1=input("enter age for employee 1")
p1=input("enter phone for employee 1")
ad1=input("enter address for employee 1")
id1=input("enter eid for employee 1")

n2=input("enter name for employee 2")
a2=input("enter age for employee 2")
p2=input("enter phone for employee 2")
ad2=input("enter address for employee 2")
id2=input("enter eid for employee 2")


emp1=Employee(n1,a1,p1,ad1,id1)
print(emp1.name, emp1.phone ,emp1.phone,emp1.address,emp1.eid)
emp1.talk()
emp1.walk()

emp2=Employee(n2,a2,p2,ad2,id2)
print(emp2.name, emp2.phone ,emp2.phone,emp2.address,emp2.eid)
emp2.talk()
emp2.walk()