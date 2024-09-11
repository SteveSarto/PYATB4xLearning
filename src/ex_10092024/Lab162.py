import os

full_path = os.path.join("steve", "steve1.txt")

file = open(full_path, 'r')
print(file.read())
