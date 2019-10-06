from django.test import TestCase

from .models import Recipe, Ingredient

class RecipeModelTests(TestCase):
    def ensure_recipe_has_ingredients_question(self):
        test_recipe = Recipe(recipe_name="Recipe", recipe_desc="Description")
    pass
class IngredientModelTests(TestCase):
    pass
# Create your tests here.
