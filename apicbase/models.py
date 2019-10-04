from django.db import models
from django.forms import ModelForm
# Create your models here.

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=100)
    ingredient_desc = models.CharField(max_length=1000)
    ingredient_cost = models.IntegerField(default=0)
    ingredient_unit_size = models.IntegerField(default=1)
    is_fluid = models.BooleanField(default=False) #used for converting to the higher denomination
                                                  # if fluid -> quantity / 100 -> liters
                                                  # else quantity / 1000 -> kilograms

    def __str__(self):
        return self.ingredient_name

        
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_desc = models.CharField(max_length=1000)
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")

    def __str__(self):
        return self.recipe_name

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class RecipeIngredient(models.Model):
    recipe_name = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0) #will store in smallest denomination(ie grams/centiliter) and convert later


