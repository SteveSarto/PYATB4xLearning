class Calci:
    def __init__(self):
        print("Calculations")
    def sum(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return  a*b
    def div(self,a,b):
        return a/b

display= Calci()

output_sum=print(display.sum(1,2))
output_sub=print(display.sub(3,4))
output_mul=print(display.mul(5,5))
output_div=print(display.div(6,7))



