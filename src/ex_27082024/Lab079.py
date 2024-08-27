#list
my_shopping_list=["bread","egg","milk"]
print(my_shopping_list)
print(len(my_shopping_list))

def bring_more_food(my_shopping_list):
    more_item=input("enter item")
    my_shopping_list.append(more_item)

    my_shopping_list.remove("milk")
    my_shopping_list.insert(0,"dryfruit")
    return my_shopping_list

l=bring_more_food(my_shopping_list)
print(l)