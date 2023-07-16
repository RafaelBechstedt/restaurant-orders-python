import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self._load_menu_data(source_path)

    def _load_menu_data(self, source_path: str) -> None:
        with open(source_path, "r") as file:
            reader = csv.DictReader(file)
            dishes = {}

            for row in reader:
                dish_name = row["dish"]
                dish_price = float(row["price"])
                ingredient_name = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                if dish_name not in dishes:
                    dish = Dish(dish_name, dish_price)
                    dishes[dish_name] = dish
                    self.dishes.add(dish)
                else:
                    dish = dishes[dish_name]

                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, recipe_amount)
