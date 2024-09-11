#finding path for file
import os
try:
    full_path =os.getcwd()
    full_path_file = full_path+"/example.txt"
    print(full_path_file)


    file = open(full_path_file, 'r')
    print(file.read())
except Exception as fl:
    print("creat a file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)