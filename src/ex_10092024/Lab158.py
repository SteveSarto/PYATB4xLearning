# Custo exception

class LowBalanceExep(Exception):
    def __init__(self,message):
        self.message= message
        super().__init__(message)


balance = 200
withdrawal=int(input("enter withdrawl amount"))
if withdrawal > balance:
    raise LowBalanceExep("low balance")
else:
    print("availanle balnae is",(balance- withdrawal))

