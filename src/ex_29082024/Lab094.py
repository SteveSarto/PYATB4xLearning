#List
my_list =[1,2,3,4]

print(my_list)

print(len(my_list))

print(my_list[0])

my_list[0]="Steve"

print(my_list)

my_list.append("Sarto")
print(my_list)

my_list.extend([7,9,8])
print(my_list)
my_list.insert(1,"Sarto")
print(my_list)

#- instert give reverse

my_list.insert(-1,"steny")
print(my_list)

print("----------------------")

my_copy_list = my_list.copy()
print(my_copy_list)
print(my_list)
print("----------------------")

my_list.clear()
print(my_copy_list)
print(my_list)
print("----------------------")
#my_copy_list.sort()
#print(my_copy_list)

my_copy_list.remove("Steve")
print(my_copy_list)
my_copy_list.remove("steny")
print(my_copy_list)
my_copy_list.remove("Sarto")
print(my_copy_list)
my_copy_list.remove("Sarto")
print(my_copy_list)

print("----------------------")
my_copy_list.sort()
print(my_copy_list)

my_copy_list.reverse()
print(my_copy_list)