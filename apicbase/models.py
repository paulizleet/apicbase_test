from django.db import models
from django.forms import ModelForm, Textarea
from django import forms
# Create your models here.

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=100, unique=True)
    ingredient_desc = models.CharField(max_length=1000)
    ingredient_cost = models.IntegerField(default=0)
    ingredient_unit_size = models.IntegerField(default=1)
    is_fluid = models.BooleanField(default=False) #used for converting to the higher denomination
                                                  # if fluid -> quantity / 100 -> liters
                                                  # else quantity / 1000 -> kilograms

    def __str__(self):
        return self.ingredient_name



class IngredientChoiceField(forms.Form):
    field1 = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all())



class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class RecipeIngredient(models.Model):
    #recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0) #will store in smallest denomination(ie grams/centiliter) and convert later

    #don't store cost in table because it's subject to change
    def get_cost(self):
        #divide this all by 100 to convert from cents to euros
        return ((self.quantity / self.ingredient.ingredient_unit_size) * self.ingredient.ingredient_cost)/100


    def get_measure(self):

        # Logic to return liters/grams for liquids/solids
        # and convert into higher denominations if need be

        # I assume that people arent using thousands 
        # of kilograms of stuff in a single recipe
        measure = ""
        quantity = self.quantity
        if self.ingredient.is_fluid:
            measure = "L"
            if quantity < 100:
                measure = "cL"
            else:
                quantity /= 100
        else:
            measure = "g"
            if quantity >= 1000:
                measure = "kg"
                quantity /= 1000

        return "%s %s" % (quantity, measure)
        
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100, unique=True)
    recipe_desc = models.CharField(max_length=1000)
    ingredients = models.ManyToManyField(RecipeIngredient)

    def __str__(self):
        return self.recipe_name

    def assemble_for_display(self):
        #prepare a nice packet of relevant data for ez insertion into a template

        data = {}
        
        total_cost = 0
        for rec_ingredient in self.ingredients.all():
            ing_cost = rec_ingredient.get_cost()
            data[rec_ingredient]=ing_cost
            total_cost += ing_cost


        #silliness to return two values at once, preventing 
        # an extra blank table row in the template
        return [data, total_cost]


    def add_ingredient(self, ing, quantity):
        ingredient = Ingredient.objects.get(id=ing)
        recing = RecipeIngredient(ingredient=ingredient, quantity=quantity)
        recing.save()
        self.ingredients.add(recing)

class RecipeForm(ModelForm):

    
    ingredient_choices = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all())

    # ingredient_choices = IngredientChoiceField()
    class Meta:
        model = Recipe
        fields = ["recipe_name", "recipe_desc"] #don't use default behavior for ingredients field.  it's special

    #override
    def save(self):
        pass
        
