#task6
def user_shopping(s_list):
    for element in s_list:
        print("You bought: ",element)

shopping_list = []

while True:
    items = input("\nEnter the item you bought from market \nIf you leave enter'exit': ")
    if items == 'exit':
        break
    shopping_list.append(items)

user_shopping(shopping_list)