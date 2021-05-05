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
                categoryOrder = input("Please enter the order this item should be added in the list: ")
                print(" ")
                print(" ")
                print(list(enumerate(categoryOrderList)))
                print(" ")
                print(" ")
                categoryOrderList.insert(int(categoryOrder), itemCategory)
                categoryOrderDict = {x: i for i, x in enumerate(categoryOrderList)}
                
    # if addItem input is "DONE", sort shoppingLst using the fitness function to sort the items and then print the list
    else:
        print("Your shopping list contains: ")
        shoppingLst.sort(key=fitness)
        for items in shoppingLst:
            print(items)
        break 

#loop: take user user input to add/edit/remove items in/to the shopping list. [aer = add/edit/remove]
while True:
    aerLst = input("To add another item to the shopping list list, enter 1. To remove an item from the list, enter 2. To finish your list, enter 3.: ")

    #add new item to the list
    if aerLst == "1":
        addNewItem = input("what would you like to add to your shopping list? ")
        
        #same code to add a new item as initial input set from user
        if addNewItem != "DONE":
            shoppingLst.append(addNewItem)

            if addNewItem not in itemCategoryDict:
                itemCategory = input("No category exists for this item. Please enter the category for this item: ")
                itemCategoryDict[addNewItem] = itemCategoryDict

                if itemCategory not in categoryOrderDict:
                    categoryOrder = input("Please enter the order this item should be added in the list: ")
                    print(" ")
                    print(" ")
                    for items in list(enumerate(categoryOrderList)):
                        print(items)
                    print(" ")
                    print(" ")
                    categoryOrderList.insert(int(categoryOrder), itemCategory)
                    categoryOrderDict = {x: i for i, x in enumerate(categoryOrderList)}
                    continue

    #removes an item from the shopping list
    #[NOTE] NOT DONE; NEED TO ACTUALLY WRITE CODE THAT REMOVES THE ITEM
    if aerLst == "2":
        while True:
            print("please enter the item you would like to remove from your shopping list")

            for items in shoppingLst:
                print(items)

            removeItem = input()
            if removeItem not in itemCategoryDict: 
                print("that item is not in your shopping list!")
                continue
            else:
                shoppingLst.remove(removeItem)
                break
        continue

    if aerLst == "3":
        print("This is your shopping list: ")
        for items in shoppingLst:
            print(items)
        break
