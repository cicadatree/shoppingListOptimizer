
categoryOrderList = ["processed goods", "deli", "processed produce", "produce (fruits)", "produce (watered vegetables)", "produce (vegetables)", "produce (root vegetables)", "gluten products", "seafood", "butchered meats", "processed meats", "dairy", "processed frozen", "aisles"]

categoryOrderDict = {x: i for i, x in enumerate(categoryOrderList)}

itemCategoryDict = {
    'apple': 'produce (fruits)',
    'orange': 'produce (fruits)',
    'swiss chard': 'produce (watered vegetables)',
    'brocolli': 'produce (watered vegetables)',
    'garlic': 'produce (vegetables)',
    'onion': 'produce (vegetables)',
    'potatoe': 'produce (root vegetables)',
    'yam': 'produce (root vegetables)',
    'whole wheat pita': 'gluten products',
    'rye bread': 'gluten products',
    'smoked salmon': 'pseafood',
    'live lobster': 'seafood',
    'ribeye steak': 'butchered meats'
    'porkchops': 'butchered meats',
    'packaged bacon': 'processed meats',
    'hotdogs': 'processed meats',
    'eggs': 'dairy',
    'milk': 'dairy',
    'frozen dumplings': 'processed frozen',
    'frozen fruit': 'processed frozen'
}