
import data

class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, amount in ingredients.items():
            if ingredient not in self.machine_resources or self.machine_resources[ingredient] < amount:
                return False
        return True

    def make_sandwich(self, sandwich_size):

        recipe = data.recipes.get(sandwich_size)
        if recipe is None:
            print(f"Error: Sandwich size '{sandwich_size}' is not available.")
            return False

        if self.check_resources(recipe['ingredients']):
            print(f"Making {sandwich_size} sandwich...")
            for ingredient, amount in recipe['ingredients'].items():
                self.machine_resources[ingredient] -= amount
            return True
        else:
            print("Insufficient resources to make the sandwich.")
            return False