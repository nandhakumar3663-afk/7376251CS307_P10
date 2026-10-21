class Recipe_book:

    def __init__(self):
        self.recipe_queue = []

    def menu(self):
        print()
        print("============== Menu ================")
        print("1. Lemon Juice")
        print("2. Tea")
        print("3. Coffee")
        print("4. Tomato Rice")
        print("5. Chocolate Milkshake")

    def recipe_instructions(self, num):
        recipes = {
            1: {
                "name": "Lemon Juice",
                "preparation_time": "5 minutes",
                "cooking_time": "0 minutes",
                "servings": "1 glass",
                "ingredients": [
                    "1 medium lemon",
                    "250 ml cold water",
                    "2 teaspoons sugar",
                    "A pinch of salt (optional)",
                    "Ice cubes (optional)"
                ],
                "steps": [
                    "Wash the lemon thoroughly with water.",
                    "Cut the lemon into two halves.",
                    "Squeeze the lemon and remove the seeds.",
                    "Pour 250 ml of cold water into a glass.",
                    "Add 2 teaspoons of sugar and stir well.",
                    "Add a pinch of salt if desired.",
                    "Add ice cubes and serve."
                ]
            },

            2: {
                "name": "Tea",
                "preparation_time": "2 minutes",
                "cooking_time": "8 minutes",
                "servings": "2 cups",
                "ingredients": [
                    "250 ml water",
                    "250 ml milk",
                    "2 teaspoons tea powder",
                    "2-3 teaspoons sugar",
                    "2 cardamom pods (optional)"
                ],
                "steps": [
                    "Boil water in a saucepan.",
                    "Add tea powder and crushed cardamom.",
                    "Boil for 2-3 minutes.",
                    "Add milk and stir well.",
                    "Add sugar according to taste.",
                    "Simmer for another 3-4 minutes.",
                    "Strain the tea into cups.",
                    "Serve hot."
                ]
            },

            3: {
                "name": "Coffee",
                "preparation_time": "2 minutes",
                "cooking_time": "5 minutes",
                "servings": "1 cup",
                "ingredients": [
                    "250 ml milk",
                    "1 teaspoon instant coffee powder",
                    "1-2 teaspoons sugar",
                    "2 tablespoons hot water"
                ],
                "steps": [
                    "Heat the milk in a saucepan.",
                    "Add coffee powder to a cup.",
                    "Pour 2 tablespoons of hot water into the cup.",
                    "Stir until the coffee powder dissolves.",
                    "Add sugar according to taste.",
                    "Pour the hot milk into the cup.",
                    "Mix everything well.",
                    "Serve hot."
                ]
            },

            4: {
                "name": "Tomato Rice",
                "preparation_time": "10 minutes",
                "cooking_time": "20-25 minutes",
                "servings": "2 people",
                "ingredients": [
                    "1 cup raw rice",
                    "3 medium tomatoes, chopped",
                    "1 medium onion, sliced",
                    "1 green chilli",
                    "1 teaspoon ginger-garlic paste",
                    "2 tablespoons cooking oil",
                    "1/2 teaspoon mustard seeds",
                    "1/2 teaspoon turmeric powder",
                    "1 teaspoon chilli powder",
                    "1/2 teaspoon garam masala (optional)",
                    "A few curry leaves",
                    "Salt to taste",
                    "1 3/4 to 2 cups water, as needed",
                    "Coriander leaves (optional)"
                ],
                "steps": [
                    "Wash the rice two or three times and drain the water.",
                    "Chop the tomatoes and slice the onion.",
                    "Heat oil in a pot or pressure cooker.",
                    "Add mustard seeds and allow them to splutter.",
                    "Add curry leaves, onion and green chilli.",
                    "Saute until the onion becomes soft.",
                    "Add ginger-garlic paste and cook for one minute.",
                    "Add chopped tomatoes and cook until soft.",
                    "Add turmeric powder, chilli powder, garam masala and salt.",
                    "Add the washed rice and mix gently.",
                    "Pour in the appropriate amount of water.",
                    "Cover and cook until the rice is tender.",
                    "Release pressure safely if using a pressure cooker.",
                    "Let the rice rest for 5 minutes.",
                    "Garnish with coriander leaves and serve."
                ]
            },

            5: {
                "name": "Chocolate Milkshake",
                "preparation_time": "5 minutes",
                "cooking_time": "0 minutes",
                "servings": "1 large glass",
                "ingredients": [
                    "250 ml chilled milk",
                    "2 tablespoons chocolate syrup",
                    "1 tablespoon cocoa powder",
                    "1-2 teaspoons sugar (optional)",
                    "1 scoop chocolate or vanilla ice cream (optional)",
                    "Chocolate shavings (optional)"
                ],
                "steps": [
                    "Make sure the blender jar is clean.",
                    "Pour chilled milk into the blender.",
                    "Add chocolate syrup and cocoa powder.",
                    "Add sugar if desired.",
                    "Add ice cream for a creamier texture, if desired.",
                    "Close the blender lid securely.",
                    "Blend for 30-45 seconds until smooth.",
                    "Drizzle chocolate syrup inside a glass.",
                    "Pour the milkshake into the glass.",
                    "Garnish with chocolate shavings and serve immediately."
                ]
            }
        }


        if num in recipes:
            selected_recipe = recipes[num]

            print("\n========== Recipe Details ==========")
            print("Recipe Name:", selected_recipe["name"])
            print("Preparation Time:", selected_recipe["preparation_time"])
            print("Cooking Time:", selected_recipe["cooking_time"])
            print("Servings:", selected_recipe["servings"])

            print("\nIngredients:")
            for ingredient in selected_recipe["ingredients"]:
                print("-", ingredient)

            print("\nStep-by-Step Instructions:")
            for i, step in enumerate(selected_recipe["steps"], start=1):
                print(f"{i}. {step}")

            print("====================================")


            choice = input(
                "\nAdd this recipe to the cooking queue? (y/n): "
            ).lower()

            if choice == "y":
                self.recipe_queue.append(selected_recipe)
                print(selected_recipe["name"], "added to the queue.")
            elif choice == "n":
                print("Recipe not added to the queue.")
            else:
                print("Invalid choice. Recipe not added to the queue.")

        else:
            print("Invalid recipe number! Please enter a number from 1 to 5.")

    def recipe_selection(self):
        print()
        self.menu()

        try:
            num = int(input("Enter the recipe number (1-5): "))
            self.recipe_instructions(num)

        except ValueError:
            print("Invalid option! Please enter a number.")


    def view_queue(self):
        print("\n========== Cooking Queue ==========")

        if len(self.recipe_queue) == 0:
            print("The queue is empty.")
        else:
            for i, recipe_name in enumerate(self.recipe_queue, start=1):
                print(f"{i}. {recipe_name}")

        print("===================================")



    def prepare_next(self):
        print("\n========== Prepare Next Recipe ==========")

        if len(self.recipe_queue) == 0:
            print("No recipes in the queue.")

        else:
            next_recipe = self.recipe_queue.pop(0)

            print("\nNow preparing:", next_recipe["name"])
            print("Preparation Time:", next_recipe["preparation_time"])
            print("Cooking Time:", next_recipe["cooking_time"])
            print("Servings:", next_recipe["servings"])

            print("\nIngredients:")
            for ingredient in next_recipe["ingredients"]:
                print("-", ingredient)

            print("\nStep-by-Step Instructions:")
            for i, step in enumerate(next_recipe["steps"], start=1):
                print(f"{i}. {step}")

            print("\nRecipe preparation instructions completed!")
            print("Recipe removed from the queue.")

        print("=========================================")



recipe = Recipe_book()

while True:
    print("\n============ Recipe Book ============")
    print("1. View Recipe Menu")
    print("2. Select a Recipe")
    print("3. View Cooking Queue")
    print("4. Prepare Next Recipe")
    print("5. Exit")
    print("=====================================")

    try:
        val = int(input("Enter the option (1-5): "))

        if val == 1:
            recipe.menu()

        elif val == 2:
            recipe.recipe_selection()

        elif val == 3:
            recipe.view_queue()

        elif val == 4:
            recipe.prepare_next()

        elif val == 5:
            print("Thank you for using the Recipe Book!")
            break

        else:
            print("Invalid option! Enter a number from 1 to 5.")

    except ValueError:
        print("Invalid input! Please enter a number.")
