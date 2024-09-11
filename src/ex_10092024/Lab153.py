try:
    a = int(input("enter num 1"))
    b = int(input("enter num2"))
    c = a / b

except ValueError as ve:
    print("enter integer")
except ZeroDivisionError as de:
    print("dont use zero")
else:
    print("answer is", c)
finally:
    print("im always printed")