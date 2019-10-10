from django.db import models
from django.forms import ModelForm, Textarea
from django import forms
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from decimal import Decimal
# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=1000)
    cost = models.DecimalField(       
        max_digits=10,
        decimal_places=2
        )
    unit_size = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    is_fluid = models.BooleanField(default=False) # Used for converting to the higher denomination
                                                  # if fluid -> quantity / 100 -> liters
                                                  # else quantity / 1000 -> kilograms

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('apicbase:ingredient-detail', kwargs={"pk":self.id})

    def get_unit_size(self):

        # Logic to return liters/grams for liquids/solids
        # and convert into higher denominations if need be

        # I assume that people arent using thousands 
        # of kilograms of stuff in a single recipe
        measure = ""
        quantity = self.unit_size
        if self.is_fluid:
            measure = "L"
            if quantity < 100:
                measure = "cL"
            else:
                quantity = round((quantity / 100), 1) #truncate to 1 decimal place
        else:
            measure = "g"
            if quantity >= 1000:
                measure = "kg"
                quantity = round((quantity / 1000), 1) #truncate to 1 decimal place

        return "%s %s" % (quantity, measure)




class IngredientForm(ModelForm):

    # Override form labels and give our form fields Bootstrap styling
    name = forms.CharField(
        label="Ingredient Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    desc = forms.CharField(
        max_length=1000,
        label="Description",
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    
    cost = forms.DecimalField(
        label = "Cost per unit (€)",
        min_value=0,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'class':'form-control'
            }
        )
    )


    unit_size = forms.IntegerField(
        label="Unit size (cL/g)",

        widget=forms.NumberInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    is_fluid = forms.BooleanField(
        label = "Is liquid?",
        required=False
    )



    class Meta:
        model = Ingredient
        fields = "__all__"



class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0) #will store in smallest denomination(ie grams/centiliter) and convert later

    #Don't store cost in table because it's subject to change
    def get_cost(self):
        # Divide this all by 100 to convert from cents to euros
        # Truncate to 2 decimal places
        return round(((Decimal( self.quantity / self.ingredient.unit_size ))  * self.ingredient.cost), 2)

    # Whenever we refer to this model, we only really care about the ingredient
    # so we return values for that instead of whatever defaults we get for this model
    def get_absolute_url(self):
        return reverse("apicbase:ingredient-detail", kwargs={"pk": self.ingredient.pk})

    # Shortens calls from RecipeIngredient.ingredient.name to RecipeIngredient.name
    def name(self):
        return self.ingredient.name

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
                quantity = round((quantity / 100), 1) #truncate to 1 decimal place
        else:
            measure = "g"
            if quantity >= 1000:
                measure = "kg"
                quantity = round((quantity / 1000), 1) #truncate to 1 decimal place

        return "%s %s" % (quantity, measure)


class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=1000)
    ingredients = models.ManyToManyField(RecipeIngredient)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("apicbase:recipe-detail", kwargs={"pk":self.id})


    def assemble_for_display(self):
        #prepare a nice packet of relevant data for ez insertion into a template

        data = {}
        
        total_cost = 0
        for rec_ingredient in self.ingredients.all():
            ing_cost = rec_ingredient.get_cost()
            data[rec_ingredient]='%.2f'.zfill(1) % (ing_cost)
            total_cost += ing_cost


        #silliness to return two values at once, preventing 
        # an extra blank table row in the template
        return [data, total_cost]

    def add_ingredients(self, ingredient_string):
        # Takes the ingredient form data and makes adds all ingredients
        errors = []
        for each in ingredient_string.split(";"):
            #  each looks something like "123,987"
            #  split[0] is the ingredient id
            #  split[1] is the quantity
            try:
                splits = each.split(",")
                if int(splits[1]) < 1:
                    raise ValidationError

                self.add_ingredient(ing=splits[0], quantity=splits[1])
            except IndexError:
                #  since these strings will always end with a trailing ';', 
                #  it will cause an exception when the final split piece is ''
                #  we don't need the loop anymore so we jump out of it
                break


    def add_ingredient(self, ing, quantity):
        ingredient = Ingredient.objects.get(id=ing)
        recing = RecipeIngredient(ingredient=ingredient, quantity=quantity)
        recing.save()
        self.ingredients.add(recing)

class RecipeForm(ModelForm):


    # Override form labels and give our form fields Bootstrap styling
    name = forms.CharField(
        label="Recipe Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    desc = forms.CharField(
        max_length=1000,
        label="Description",
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
      
        )
    )
    ingredient_choices = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                'class':'custom-select'
            }
        ),
        required=False
    )

    class Meta:
        model = Recipe
        fields = ["name", "desc"] #don't use default behavior for ingredients field.  it's special

class SearchForm(forms.Form):
    search_text = forms.CharField(
        required=True,
        #label='Search for recipes or ingredients',
        widget = forms.TextInput(attrs={'placeholder': 'Search for recipes or ingredients'})
    )
        