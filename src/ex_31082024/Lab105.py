class person:
         id =  None
         name= None
         email= None
         age =None
         height=None
         gender=None

         def talk (self):
            print("i can talk")

         def sleep (self,name):
             print("i can sleep")
             print("i sleep", name)
         def sleep2 (self,name):
              print("i can sleep again")
              return None
         def walk (self):
              print("i can walk")
         def walk_return (self):
              print("i can walk again")


steve = person()
steve.name = "steve"
print(steve.name)
steve.talk()