class XYZ:
    def z(self):
        try:
            a = int(input("enter number"))
        except Exception as e:
            print(e)
        else:
            print(a)
        finally:
            print("i willbe printed")
x=XYZ()
x.z()