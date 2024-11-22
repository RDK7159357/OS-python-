from collections import OrderedDict

class CafeRecipeBook:
    def __init__(self, capacity):
        """
        Initialize the CafeRecipeBook with a given capacity.
        """
        self.capacity = capacity
        self.recipes = OrderedDict()  # To maintain insertion order and handle updates efficiently

    def add_recipe(self, recipe):
        """
        Add a recipe to the recipe book. If the recipe already exists,
        move it to the end (most recent). If the capacity is exceeded,
        remove the oldest recipe.
        """
        if recipe in self.recipes:
            # Move existing recipe to the end
            self.recipes.move_to_end(recipe)
        else:
            if len(self.recipes) == self.capacity:
                # Remove the oldest recipe
                removed_recipe = self.recipes.popitem(last=False)
                print(f"Removed recipe: {removed_recipe[0]}")
            # Add the new recipe
            self.recipes[recipe] = True

    def display_recipes(self):
        """
        Display the recipes currently in the book.
        """
        if not self.recipes:
            print("The recipe book is empty.")
        else:
            print("Recipes in the book:")
            for recipe in self.recipes.keys():
                print(f"- {recipe}")


# Driver Code
cafe_recipe_book = CafeRecipeBook(capacity=2)
recipes = [
    "Pumpkin Spice Latte",
    "Apple Pie",
    "Blueberry Muffin",

]

for recipe in recipes:
    cafe_recipe_book.add_recipe(recipe)

cafe_recipe_book.display_recipes()
