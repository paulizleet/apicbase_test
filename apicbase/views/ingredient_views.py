from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from apicbase.models import Ingredient, IngredientForm, RecipeIngredient, Recipe
from django.http import HttpResponse
from django.core.paginator import Paginator


class IngredientIndex(ListView):
    template_name = 'ingredients/index.html'

    def get(self, request):
        #Grabs all ingredients and paginates them before serving
        ingredient_list = Ingredient.objects.all()
        paginator = Paginator(ingredient_list, 10)
        page_num = 0
        page_num = request.GET.get("page")
        ingredients = paginator.get_page(page_num)
        
        # pass in page_nums so I can iteratively make page number links
        return render(request, self.template_name, {'ingredients': ingredients, 'page_nums': range(1, paginator.num_pages+1)})


    def get_queryset(self):
        return Ingredient.objects.all()[:20]

class IngredientDetail(DetailView):
    model = Ingredient
    template_name = "ingredients/detail.html"

    def get(self, request, pk):
        # Grabs the requested ingredient and all recipes containing that ingredient
        ingredient = Ingredient.objects.get(id=pk)
        recipes = Recipe.objects.filter(ingredients__ingredient=ingredient)

        return render(request, self.template_name, {'ingredient': ingredient, 'recipes': recipes})


class IngredientCreate(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredients/ingredient_create_page.html"
    

class IngredientUpdate(UpdateView):

    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredients/ingredient_create_page.html"

    def form_valid(self, form):
        form.save()
        return redirect("/ingredient/%s" % self.kwargs["pk"])
