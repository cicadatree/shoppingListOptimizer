from MasterIndex import masterIndexDict

shoppingList = []
quitShop = False

# NOT DONE: function that sorts items in shoppingList so that items are optimized based on store layout
def storeSort(shoppingList):

    #iterate through the new shopping list dictionary
    for key, value in enumerate(shoppingList):
        print(key)

        match = True
        if not key in masterIndexDict or enumerate(shoppingList)[key] != masterIndexDict[key]:
            match = False
    return storeSort

while quitShop == False:

    #add the user's inputted shopping list item to shoppingList
    addItem = input("Please enter your shopping list items here (when finished, enter DONE): ")
    shoppingList.append(addItem)

    #break the loop if the user inputs "DONE"
    if addItem == "DONE":
        storeSort(shoppingList)
        print("Your shopping list contains: ")
        for items in shoppingList[:-1]:
            print(items)
        break