from apicbase.models import Recipe, Ingredient, RecipeIngredient


Ingredient(
    name = "Mozzarella",
    desc = "String cheese",
    cost = "1.00",
    unit_size = "500" ,
    is_fluid = False
).save()

Ingredient(
    name = "Flour",
    desc = "Good in bread",
    cost = "0.50",
    unit_size = "1000" ,
    is_fluid = False
).save()


Ingredient(
    name = "Tomato Sauce",
    desc = "Sauce made of Tomatos",
    cost = "5.00",
    unit_size = "1000" ,
    is_fluid = True
).save()

Ingredient(
    name = "Pepperoni",
    desc = "Spicy sausage good on pizza",
    cost = "6.00",
    unit_size = "1000" ,
    is_fluid = False
).save()

peppizza = Recipe(
    name="Pepperoni Pizza",
    desc="Pizza with pepperonis on it"
).save()

ingredient = Ingredient.objects.get(name="Mozzarella")
recing = RecipeIngredient(ingredient=ingredient, quantity=500)
recing.save()
peppizza.ingredients.add(recing)


ingredient = Ingredient.objects.get(name="Tomato Sauce")
recing = RecipeIngredient(ingredient=ingredient, quantity=500)
recing.save()
peppizza.ingredients.add(recing)


ingredient = Ingredient.objects.get(name="Pepperoni")
recing = RecipeIngredient(ingredient=ingredient, quantity=300)
recing.save()
peppizza.ingredients.add(recing)

ingredient = Ingredient.objects.get(name="Flour")
recing = RecipeIngredient(ingredient=ingredient, quantity=1000)
recing.save()
peppizza.ingredients.add(recing)


peppizza.save()

pizza = Recipe(
    name="Cheese Pizza",
    desc="Pizza with no toppings"
)
pizza.save()
ingredient = Ingredient.objects.get(name="Mozzarella")
recing = RecipeIngredient(ingredient=ingredient, quantity=500)
recing.save()
pizza.ingredients.add(recing)


ingredient = Ingredient.objects.get(name="Tomato Sauce")
recing = RecipeIngredient(ingredient=ingredient, quantity=500)
recing.save()
pizza.ingredients.add(recing)

ingredient = Ingredient.objects.get(name="Flour")
recing = RecipeIngredient(ingredient=ingredient, quantity=1000)
recing.save()
pizza.ingredients.add(recing)


pizza.save()