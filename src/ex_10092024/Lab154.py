import os
try:
    file = open('example.txt', 'r')
    print(file.read())
except Exception as fl:
    print("creat a file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)



