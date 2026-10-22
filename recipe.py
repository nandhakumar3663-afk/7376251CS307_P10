
RECIPES_FILE = "recipes.txt"
INGREDIENTS_FILE = "ingredients.txt"
STEPS_FILE = "steps.txt"


def load_recipes():
    recipes = []

    try:
        file = open(RECIPES_FILE, "r", encoding="utf-8")
        lines = file.readlines()
        file.close()
    except OSError:
        print("Error: recipes.txt was not found.")
        return recipes

    for line in lines:
        line = line.strip()
        if line == "" or line.startswith("RecipeID|"):
            continue

        parts = line.split("|")
        if len(parts) == 5:
            try:
                recipe = {
                    "id": parts[0],
                    "name": parts[1],
                    "cuisine": parts[2],
                    "prep": int(parts[3]),
                    "servings": int(parts[4]),
                    "ingredients": [],
                    "steps": []
                }
                recipes.append(recipe)
            except ValueError:
                print("Skipping an invalid recipe record.")

    try:
        file = open(INGREDIENTS_FILE, "r", encoding="utf-8")
        lines = file.readlines()
        file.close()
    except OSError:
        print("Error: ingredients.txt was not found.")
        return recipes

    for line in lines:
        line = line.strip()
        if line == "" or line.startswith("RecipeID|"):
            continue

        parts = line.split("|")
        if len(parts) != 4:
            continue

        try:
            quantity = float(parts[1])
        except ValueError:
            continue

        for recipe in recipes:
            if recipe["id"] == parts[0]:
                recipe["ingredients"].append({
                    "quantity": quantity,
                    "unit": parts[2],
                    "name": parts[3]
                })
                break

    try:
        file = open(STEPS_FILE, "r", encoding="utf-8")
        lines = file.readlines()
        file.close()
    except OSError:
        print("Error: steps.txt was not found.")
        return recipes

    for line in lines:
        line = line.strip()
        if line == "" or line.startswith("RecipeID|"):
            continue

        parts = line.split("|")
        if len(parts) != 3:
            continue

        try:
            step_number = int(parts[1])
        except ValueError:
            continue

        for recipe in recipes:
            if recipe["id"] == parts[0]:
                recipe["steps"].append((step_number, parts[2]))
                break

    for recipe in recipes:
        recipe["steps"].sort()

    return recipes


def save_recipes(recipes):
    """Write all recipe data back to the text files."""

    file = open(RECIPES_FILE, "w", encoding="utf-8")
    file.write("RecipeID|Name|Cuisine|PrepMinutes|Servings\n")
    for recipe in recipes:
        file.write(
            recipe["id"] + "|" + recipe["name"] + "|" +
            recipe["cuisine"] + "|" + str(recipe["prep"]) + "|" +
            str(recipe["servings"]) + "\n"
        )
    file.close()

    file = open(INGREDIENTS_FILE, "w", encoding="utf-8")
    file.write("RecipeID|Quantity|Unit|Ingredient\n")
    for recipe in recipes:
        for item in recipe["ingredients"]:
            file.write(
                recipe["id"] + "|" + str(item["quantity"]) + "|" +
                item["unit"] + "|" + item["name"] + "\n"
            )
    file.close()

    file = open(STEPS_FILE, "w", encoding="utf-8")
    file.write("RecipeID|StepNo|Instruction\n")
    for recipe in recipes:
        for number, instruction in recipe["steps"]:
            file.write(
                recipe["id"] + "|" + str(number) + "|" +
                instruction + "\n"
            )
    file.close()


def find_recipe(recipes, search_text):
    """Find a recipe by ID or name."""
    search_text = search_text.strip().lower()

    for recipe in recipes:
        if recipe["id"].lower() == search_text:
            return recipe
        if recipe["name"].lower() == search_text:
            return recipe

    return None


def list_recipes(recipes):
    print("\n--- ALL RECIPES ---")
    if len(recipes) == 0:
        print("No recipes found.")
        return

    for recipe in recipes:
        print(recipe["id"], "-", recipe["name"])
    print("Total recipes:", len(recipes))


def show_recipe(recipes):
    recipe = find_recipe(recipes, input("Enter recipe ID or name: "))
    if recipe is None:
        print("Recipe not found.")
        return

    print("\n---", recipe["name"], "---")
    print("Cuisine:", recipe["cuisine"])
    print("Preparation time:", recipe["prep"], "minutes")
    print("Servings:", recipe["servings"])

    print("\nIngredients:")
    for item in recipe["ingredients"]:
        print("-", item["quantity"], item["unit"], item["name"])

    print("\nSteps:")
    for number, instruction in recipe["steps"]:
        print(str(number) + ".", instruction)


def add_recipe(recipes):
    print("\n--- ADD RECIPE ---")
    name = input("Recipe name: ").strip()
    cuisine = input("Cuisine: ").strip()

    if name == "" or cuisine == "":
        print("Name and cuisine cannot be empty.")
        return

    try:
        prep = int(input("Preparation time in minutes: "))
        servings = int(input("Number of servings: "))
    except ValueError:
        print("Enter whole numbers for time and servings.")
        return

    if prep <= 0 or servings <= 0:
        print("Time and servings must be greater than zero.")
        return

    ingredients = []
    print("Enter ingredients. Press Enter on a blank name to finish.")

    while True:
        name_of_ingredient = input("Ingredient name: ").strip()
        if name_of_ingredient == "":
            break

        try:
            quantity = float(input("Quantity: "))
        except ValueError:
            print("Invalid quantity. Try again.")
            continue

        unit = input("Unit (cup, pcs, tbsp, etc.): ").strip()
        ingredients.append({
            "quantity": quantity,
            "unit": unit,
            "name": name_of_ingredient
        })

    if len(ingredients) == 0:
        print("A recipe needs at least one ingredient.")
        return

    steps = []
    print("Enter steps. Press Enter on a blank step to finish.")

    while True:
        instruction = input("Step " + str(len(steps) + 1) + ": ").strip()
        if instruction == "":
            break
        steps.append((len(steps) + 1, instruction))

    if len(steps) == 0:
        print("A recipe needs at least one step.")
        return

    highest_number = 0
    for recipe in recipes:
        number = recipe["id"].replace("R", "")
        if number.isdigit() and int(number) > highest_number:
            highest_number = int(number)

    recipe_id = "R" + str(highest_number + 1).zfill(2)

    new_recipe = {
        "id": recipe_id,
        "name": name,
        "cuisine": cuisine,
        "prep": prep,
        "servings": servings,
        "ingredients": ingredients,
        "steps": steps
    }

    recipes.append(new_recipe)
    save_recipes(recipes)
    print("Recipe added. ID:", recipe_id)


def search_by_ingredient(recipes):
    search_name = input("Enter ingredient to search: ").strip().lower()
    found = False

    for recipe in recipes:
        for item in recipe["ingredients"]:
            if item["name"].lower() == search_name:
                print("-", recipe["name"], "(" + recipe["id"] + ")")
                found = True
                break

    if not found:
        print("No recipes found with that ingredient.")


def scale_recipe(recipes):
    recipe = find_recipe(recipes, input("Enter recipe ID or name: "))
    if recipe is None:
        print("Recipe not found.")
        return

    try:
        new_servings = int(input("New number of servings: "))
    except ValueError:
        print("Enter a whole number.")
        return

    if new_servings <= 0:
        print("Servings must be greater than zero.")
        return

    # Example: 5 servings / 2 original servings = 2.5 times the recipe.
    multiplier = new_servings / recipe["servings"]

    print(
        "\nScale", recipe["name"], "from", recipe["servings"],
        "to", new_servings, "servings:"
    )

    for item in recipe["ingredients"]:
        new_quantity = round(item["quantity"] * multiplier, 1)
        print(format(new_quantity, ".1f"), item["unit"], item["name"])


def what_can_i_cook(recipes):
    entered_text = input(
        "Ingredients you have (separate with commas): "
    ).lower()

    available = []
    for name in entered_text.split(","):
        name = name.strip()
        if name != "":
            available.append(name)

    if len(available) == 0:
        print("Please enter at least one ingredient.")
        return

    can_cook = []
    missing_one = []

    for recipe in recipes:
        missing = []

        for item in recipe["ingredients"]:
            name = item["name"].lower()
            if name not in available and name not in missing:
                missing.append(name)

        if len(missing) == 0:
            can_cook.append(recipe["name"])
        elif len(missing) == 1:
            missing_one.append((recipe["name"], missing[0]))

    print("\nYou can cook:")
    if len(can_cook) == 0:
        print("- No complete recipes found.")
    else:
        for name in can_cook:
            print("-", name)

    print("\nMissing one ingredient:")
    if len(missing_one) == 0:
        print("- No recipes are missing exactly one ingredient.")
    else:
        for name, missing_name in missing_one:
            print("-", name, "(missing:", missing_name + ")")


def sort_by_prep_time(recipes):

    sorted_recipes = sorted(recipes, key=lambda item: item["prep"])

    print("\n--- RECIPES BY PREPARATION TIME ---")
    for recipe in sorted_recipes:
        print(recipe["prep"], "minutes -", recipe["name"])


def edit_recipe(recipes):
    recipe = find_recipe(recipes, input("Enter recipe ID or name to edit: "))
    if recipe is None:
        print("Recipe not found.")
        return

    print("Press Enter to keep the current value.")
    new_name = input("Name [" + recipe["name"] + "]: ").strip()
    new_cuisine = input("Cuisine [" + recipe["cuisine"] + "]: ").strip()
    new_prep = input("Preparation time [" + str(recipe["prep"]) + "]: ").strip()
    new_servings = input("Servings [" + str(recipe["servings"]) + "]: ").strip()

    if new_name != "":
        recipe["name"] = new_name
    if new_cuisine != "":
        recipe["cuisine"] = new_cuisine

    try:
        if new_prep != "":
            recipe["prep"] = int(new_prep)
        if new_servings != "":
            recipe["servings"] = int(new_servings)
    except ValueError:
        print("Please enter valid whole numbers. Changes were not saved.")
        return

    if recipe["prep"] <= 0 or recipe["servings"] <= 0:
        print("Time and servings must be greater than zero.")
        return

    save_recipes(recipes)
    print("Recipe updated. You can also change ingredients or steps by deleting and adding the recipe again.")


def delete_recipe(recipes):
    recipe = find_recipe(recipes, input("Enter recipe ID or name to delete: "))
    if recipe is None:
        print("Recipe not found.")
        return

    answer = input("Delete " + recipe["name"] + "? (y/n): ").lower()
    if answer == "y":
        recipes.remove(recipe)
        save_recipes(recipes)
        print("Recipe deleted.")
    else:
        print("Deletion cancelled.")


def main():
    recipes = load_recipes()

    while True:
        print("\n========== RECIPE BOOK ==========")
        print("1. List all recipes")
        print("2. View a full recipe")
        print("3. Add a recipe")
        print("4. Search by ingredient")
        print("5. Scale a recipe")
        print("6. What can I cook?")
        print("7. Sort by preparation time")
        print("8. Edit a recipe")
        print("9. Delete a recipe")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            list_recipes(recipes)
        elif choice == "2":
            show_recipe(recipes)
        elif choice == "3":
            add_recipe(recipes)
            recipes = load_recipes()
        elif choice == "4":
            search_by_ingredient(recipes)
        elif choice == "5":
            scale_recipe(recipes)
        elif choice == "6":
            what_can_i_cook(recipes)
        elif choice == "7":
            sort_by_prep_time(recipes)
        elif choice == "8":
            edit_recipe(recipes)
            recipes = load_recipes()
        elif choice == "9":
            delete_recipe(recipes)
            recipes = load_recipes()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number from 0 to 9.")


if __name__ == "__main__":
    main()
