print("----Starting of program----")
try:
    a = int(input("enter num 1"))
    b = int(input("enter num2"))
    c = a / b
    print("answer is", c)
except Exception as e:
    print(e)
    print("we have an error dont enter string or zero")

print("----end of program----")
