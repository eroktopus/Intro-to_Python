recipes_list = []
ingredients_list = []

def take_recipe():
    name = str(input("Enter the name of the recipe: "))
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = (input("Enter the ingredients separated by commas: ").split(","))
    
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    return recipe
n = int(input("Enter the number of recipes you want to enter: "))


    # Loop n times to take n recipes from the user
for i in range(n):
        recipe = take_recipe()
        
        for ingredient in recipe['ingredients']:  
            if ingredient not in ingredients_list:
                ingredients_list.append(ingredient)
        
        # Append the recipe to the recipes list
        recipes_list.append(recipe)

for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
      recipe['difficulty'] = 'easy'
    if recipe['cooking_time'] > 10 and len(recipe['ingredients']) >= 4:
      recipe['difficulty'] = 'medium'
    if recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
      recipe['difficulty'] = 'intermediate'
    if recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
      recipe['difficulty'] = 'hard'

for recipe in recipes_list:
    print("Recipe: ", recipe["name"])
    print("Cooking Time (mins): ", recipe["cooking_time"])
    print("Ingredients: ")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty Level: ", recipe["difficulty"])

def all_ingredients():
    print("Ingredients Available Across All Recipes")
    print("________________________________________")
    ingredients_list.sort()
    for ingredient in ingredients_list:
        print(ingredient)

all_ingredients()
