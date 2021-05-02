# Trello task list: https://trello.com/c/eCT1YtjH/3-create-index-dictionary-for-sobeys-bridgeport

from MasterIndex import *

shoppingLst = ["Buns", "Milk", "Apples", "Pork Chops"]

print(shoppingLst)

def fitness(item):
    return categoryOrderDict[itemCategoryDict[item]]

while True:
    #add the user's inputted shopping list item to shoppingLst
    addItem = input("Please enter your shopping list items here (when finished, enter DONE): ")
    
    if addItem != "DONE":
        shoppingLst.append(addItem)

        if addItem not in itemCategoryDict:
            itemCategory = input("No category exists for this item. Please enter the category for this item: ")
            itemCategoryDict[addItem] = itemCategory  

            if itemCategory not in categoryOrderDict:
                print(list(enumerate(categoryOrderList)))
                
                categoryOrderList.insert(int(categoryOrder), itemCategory)
                categoryOrderDict = {x: i for i, x in enumerate(categoryOrderList)}
                print(categoryOrderDict)
    else:
        print("Your shopping list contains: ")
        shoppingLst.sort(key=fitness)
        for items in shoppingLst:
            print(items)
        break 
