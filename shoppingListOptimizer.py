from MasterIndex import *

#shoppingLst is currently has placeholder values for testing. It should normally be empty when initialized.
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
                categoryOrder = input("No order exists for this category. Please enter the order number for the category: ")
                categoryOrderList.insert(int(categoryOrder), itemCategory)
                categoryOrderDict = {x: i for i, x in enumerate(categoryOrderList)}
                print(categoryOrderDict)
    else:
        print("Your shopping list contains: ")

        shoppingLst.sort(key=fitness)
        for items in shoppingLst:
            print(items)
        break 
        


'''# NOT DONE: function that sorts items in shoppingLst so that items are optimized based on store layout
def storeSort(shoppingLst):

   #convert shoppingLst into a dictionary using lstToDctConvert()
    lstToDctConvert(shoppingLst)

    #just checking that the dict converter actually works (it does)
    print(shoppingLst)

    #iterate through the new shopping list dictionary, and check if each key is the same (or exists) compared to the masterIndexDict
    for key in shoppingLst:
        match = True
        if not key in masterIndexDct:
            match = False
    return '''
