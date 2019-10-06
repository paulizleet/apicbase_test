from apicbase.models import Recipe, Ingredient, RecipeIngredient


Ingredient(
    ingredient_name = "Mozzarella",
    ingredient_desc = "String cheese",
    ingredient_cost = "100",
    ingredient_unit_size = "500" ,
    is_fluid = False
).save()

Ingredient(
    ingredient_name = "Flour",
    ingredient_desc = "Good in bread",
    ingredient_cost = "50",
    ingredient_unit_size = "1000" ,
    is_fluid = False
).save()


Ingredient(
    ingredient_name = "Tomato Sauce",
    ingredient_desc = "Sauce made of Tomatos",
    ingredient_cost = "500",
    ingredient_unit_size = "1000" ,
    is_fluid = True
).save()

Ingredient(
    ingredient_name = "Pepperoni",
    ingredient_desc = "Spicy sausage good on pizza",
    ingredient_cost = "600",
    ingredient_unit_size = "1000" ,
    is_fluid = False
).save()

peppizza = Recipe(
    recipe_name="Pepperoni Pizza",
    recipe_desc="Pizza with pepperonis on it"
).save()

ingredient = Ingredient.objects.get(ingredient_name="Mozzarella")
recing = RecipeIngredient(ingredient=ingredient, quantity=500)
recing.save()
peppizza.ingredients.add(recing)


ingredient = Ingredient.objects.get(ingredient_name="Tomato Sauce")
recing = RecipeIngredient(ingredient=ingredient, quantity=500)
recing.save()
peppizza.ingredients.add(recing)


ingredient = Ingredient.objects.get(ingredient_name="Pepperoni")
recing = RecipeIngredient(ingredient=ingredient, quantity=300)
recing.save()
peppizza.ingredients.add(recing)

ingredient = Ingredient.objects.get(ingredient_name="Flour")
recing = RecipeIngredient(ingredient=ingredient, quantity=1000)
recing.save()
peppizza.ingredients.add(recing)


peppizza.save()

pizza = Recipe(
    recipe_name="Cheese Pizza",
    recipe_desc="Pizza with no toppings"
)
pizza.save()
ingredient = Ingredient.objects.get(ingredient_name="Mozzarella")
recing = RecipeIngredient(ingredient=ingredient, quantity=500)
recing.save()
pizza.ingredients.add(recing)


ingredient = Ingredient.objects.get(ingredient_name="Tomato Sauce")
recing = RecipeIngredient(ingredient=ingredient, quantity=500)
recing.save()
pizza.ingredients.add(recing)

ingredient = Ingredient.objects.get(ingredient_name="Flour")
recing = RecipeIngredient(ingredient=ingredient, quantity=1000)
recing.save()
pizza.ingredients.add(recing)


pizza.save()