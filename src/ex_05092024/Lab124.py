class Father:
    key="my house"

    def car(self):
        print("i have BMW")
class Son(Father):
    print("i own all")

father_0bj= Father()
father_0bj.key
father_0bj.car()

son_obj= Son()
son_obj.car()
son_obj.key