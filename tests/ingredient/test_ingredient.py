from models.ingredient import Ingredient, Restriction


def test_ingredient():
    # Teste inicialização ingredient
    ingredient = Ingredient("queijo mussarela")
    assert ingredient.name == "queijo mussarela"
    assert ingredient.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED}

    # Teste __repr__
    assert repr(ingredient) == "Ingredient('queijo mussarela')"

    # Teste __eq__
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")
    ingredient3 = Ingredient("farinha")
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3
    assert ingredient1 == ingredient1

    # Teste __hash__
    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient3)
