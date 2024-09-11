import os

print(os.name)
# if os.name == 'posix':
#     print("using mac")
# else:
#     print("windows")

# print(os.getcwd())
# os.chdir("/Users/promode/Downloads/postman_collections/project1")
# print(os.getcwd())
# os.mkdir('new_directory')
# os.makedirs('parent/child/grandchild')
print(os.listdir())
for file in os.listdir():
    print(file)

# os.remove('example.txt')
# os.rmdir('new_directory')

# os.rename('old_name.txt', 'new_name.txt')



