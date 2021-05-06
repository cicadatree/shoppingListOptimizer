#Bridgeport Sobeys department order:

#0. health beverages
#1. deli
#3. fruits
#4. watered vegetables
#5. vegetables
#6. root vegetables
#7. bakery
#8. seafood
#9. meat
#10. dairy
#11. frozen
#12. grocery >> grocery should really be broken out by each aisle of the store

bridgeportSobeysDepartmentOrder = ["health beverages", "deli", "fruits", "watered vegetables", "vegetables", "root vegetables", "bakery", "seafood", "meat", "dairy", "frozen", "grocery"]

departmentOrderDict = {x: i for i, x in enumerate(bridgeportSobeysDepartmentOrder)}

itemDepartmentDict = {
    'orange ginger shots': 'health beverages',
    'rotisserie chicken': 'deli',
    'scalloped potatoes': 'deli',
    'apple': 'fruits',
    'apples': 'fruits',
    'orange': 'fruits',
    'oranges': 'fruits',
    'dragon fruit': 'fruits',
    'dragon fruits': 'fruits',
    'lemon': 'fruits',
    'lemons': 'fruits',
    'pomello': 'fruits',
    'pomellos': 'fruits',
    'swiss chard': 'watered vegetables',
    'rhubarb': 'vegetables',
    'brocolli': 'watered vegetables',
    'garlic': 'vegetables',
    'onion': 'vegetables',
    'baby spinach': 'vegetables',
    'spinach': 'vegetables',
    'salad mix': 'vegetables',
    'dill': 'vegetables',
    'pistachios': 'vegetables',
    'potato': 'root vegetables',
    'potatoes': 'root vegetables',
    'yam': 'root vegetables',
    'yams': 'root vegetables',
    'everything bagles': 'bakery',
    'sesame seed bagels': 'bakery',
    'plain bagels': 'bakery',
    'white bread': 'bakery',
    'rye bread': 'bakery',
    'whole wheat bread': 'bakery',
    'ancient grain bread': 'bakery',
    'whole wheat pita': 'gluten products',
    'rye bread': 'gluten products',
    'shrimp': 'seafood',
    'shrimp cocktail': 'seafood',
    'smoked salmon': 'seafood',
    'salmon': 'seafood',
    'live lobster': 'seafood',
    'ribeye steak': 'meat',
    'ground beef': 'meat',
    'ground pork': 'meat',
    'pork chops': 'meat',
    'bacon': 'meat',
    'hotdogs': 'meats',
    'eggs': 'dairy',
    'milk': 'dairy',
    'cream': 'dairy',
    'heavy cream': 'dairy',
    'chocolate oat milk': 'dairy',
    'frozen dumplings': 'frozen',
    'frozen fruits': 'frozen',
    'frozen vegetables': 'frozen',
    'peanut butter': 'grocery',
    'capers': 'grocery',
    'breton crackers': 'grocery',
    'sidekicks': 'grocery',
    'maggi': 'grocery',
    'franks red hot sauce': 'grocery'
}