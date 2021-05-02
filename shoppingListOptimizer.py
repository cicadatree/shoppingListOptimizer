# Trello task list: https://trello.com/c/eCT1YtjH/3-create-index-dictionary-for-sobeys-bridgeport

from MasterIndex import *

shoppingLst = []

#custom sort function using MasterIndex.py as reference
def fitness(item):
    return categoryOrderDict[itemCategoryDict[item]]

#takes in user's new shopping list item input, and assigns a category & category order to it (only if the item is not already defined in MasterIndex.py)
while True:

    # add the user's inputted shopping list item to shoppingLst
    addItem = input("Please enter your shopping list items here (when finished, enter DONE): ")
    
    # if addItem input is not "DONE", append the item to shoppingLst and identify the item
    if addItem != "DONE":
        shoppingLst.append(addItem)

        # if item is not in the itemCategoryDict (see MasterIndex.py), prompt user to define a new category for it
        if addItem not in itemCategoryDict:
            itemCategory = input("No category exists for this item. Please enter the category for this item: ")
            itemCategoryDict[addItem] = itemCategory  
            
            # if the itemCategory the user has defined is not already defined in CategoryOrderDict, prompt the user to define the order that the new category should be placed
            if itemCategory not in categoryOrderDict:
                print(list(enumerate(categoryOrderList)))
                
                categoryOrderList.insert(int(categoryOrder), itemCategory)
                categoryOrderDict = {x: i for i, x in enumerate(categoryOrderList)}
                print(categoryOrderDict)

    # if addItem input is "DONE", sort shoppingLst using the fitness function to sort the items and then print the list
    else:
        print("Your shopping list contains: ")
        shoppingLst.sort(key=fitness)
        for items in shoppingLst:
            print(items)
        break 
