def recipes_list(filename: str):
    recipes_list = []

    with open(filename) as recipes_file:
        temp_list = []

        for line in recipes_file:
            line = line.replace("\n", "")

            if line!="":
                temp_list.append(line)
            else:
                recipes_list.append(temp_list[:])
                temp_list.clear()
            
        recipes_list.append(temp_list)

    return recipes_list

def search_by_name(filename: str, word: str):
    list_of_recipes = recipes_list(filename)

    recipes_with_word = []

    for recipe in list_of_recipes:
        for element in recipe:
            if word.lower() in element.lower():
                recipes_with_word.append(recipe[0])
                break

    return recipes_with_word

def search_by_time(filename: str, prep_time: int):
    list_of_recipes = recipes_list(filename)

    recipes_with_ptime = []

    for recipe in list_of_recipes:
        if prep_time>=int(recipe[1]):
            recipes_with_ptime.append(f"{recipe[0]}, preparation time {recipe[1]} min")

    return recipes_with_ptime

def search_by_ingredient(filename: str, ingredient: str):
    list_of_recipes = recipes_list(filename)

    recipes_with_ing = []

    for recipe in list_of_recipes:
        for element in recipe[2:]:
            if ingredient.lower() in element.lower():
                recipes_with_ing.append(f"{recipe[0]}, preparation time {recipe[1]} min")

    return recipes_with_ing

if __name__ == "__main__":
    found_recipes = search_by_name("recipes2.txt", "oat")

    for recipe in found_recipes:
        print(recipe)

    print()

    found_recipes = search_by_name("recipes1.txt", "cake")

    for recipe in found_recipes:
        print(recipe)

    print()

    found_recipes = search_by_time("recipes1.txt", 20)

    for recipe in found_recipes:
        print(recipe)

    print()

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)