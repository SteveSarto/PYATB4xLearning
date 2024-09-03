class Car:
    def __init__(self,o_name,o_model,o_make):
        self.name=o_name
        self.make=o_make
        self.model=o_model
    def start_engine(self):
        print("start with name",self.name)
        print("start with make",self.make)
        print("start with model",self.model)
lambo=Car("lambo","V3","US")
lambo.start_engine()
print("-----------------------")
bmw=Car("BMW","sport","Russian")
bmw.start_engine()