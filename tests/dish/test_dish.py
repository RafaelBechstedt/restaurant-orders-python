from models.ingredient import Ingredient, Restriction
from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    dish = Dish("Pastel carne e queijo", 7.50)
    # Testa propriedades de dish
    assert dish.name == "Pastel carne e queijo"
    assert dish.price == 7.50

    # Testa igualdade
    dish_2 = Dish("Pastel carne e queijo", 7.50)
    assert dish == dish_2

    dish_3 = Dish("Pastel de vento", 6.50)
    assert dish != dish_3

    # Testa get_restrictions
    ingredient_1 = Ingredient("carne")
    ingredient_2 = Ingredient("queijo mussarela")
    dish.add_ingredient_dependency(ingredient_1, 100)
    dish.add_ingredient_dependency(ingredient_2, 100)

    restrictions = dish.get_restrictions()
    assert len(restrictions) == 3
    assert Restriction.LACTOSE in restrictions
    assert Restriction.ANIMAL_MEAT in restrictions

    # Testa get_ingredients
    ingredients = dish.get_ingredients()
    assert len(ingredients) == 2
    assert ingredient_1 in ingredients
    assert ingredient_2 in ingredients

    # Testa hash
    assert hash(dish) == hash(dish_2)
    assert hash(dish) != hash(dish_3)

    # Testa repr de dish
    assert repr(dish) == "Dish('Pastel carne e queijo', R$7.50)"

    # Testa inputs inválidos
    with pytest.raises(TypeError):
        Dish("Invalid Dish", "7.50")
    with pytest.raises(ValueError):
        Dish("Invalid Dish", 0)
