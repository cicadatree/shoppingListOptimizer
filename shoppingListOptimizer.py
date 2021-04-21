from MasterIndex import masterIndexDict

shoppingLst = []
quitShop = False

#define a function to convert shoppingLst into a dictionary
def lstToDctConvert(lst):
    shoppingDct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return shoppingDct

lstToDctConvert(shoppingLst)

# NOT DONE: function that sorts items in shoppingLst so that items are optimized based on store layout
def storeSort(shoppingLst):

    #iterate through the new shopping list dictionary, and check if each key is the same (or exists) compared to the masterIndexDict
    for key in shoppingLst:
        match = True
        if not key in masterIndexDict or shoppingLst[key] != masterIndexDict[key]:
            match = False
    return 

while quitShop == False:

    #add the user's inputted shopping list item to shoppingLst
    addItem = input("Please enter your shopping list items here (when finished, enter DONE): ")
    shoppingLst.append(addItem)

    #break the loop if the user inputs "DONE"
    if addItem == "DONE":
        storeSort(shoppingLst)
        print("Your shopping list contains: ")
        for items in shoppingLst[:-1]:
            print(items)
        break 