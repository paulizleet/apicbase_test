from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse

from .models import Recipe, RecipeForm

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'recipes/index.html'

    def get_queryset(self):
        return Recipe.objects.all()[:20]
        

class DetailView(generic.DetailView):
    model = Recipe
    template_name = "recipes/detail.html"

class RecipeCreate(generic.edit.CreateView):
    model = Recipe
    
    def get(self, request):
        print("asdf")
        return render(request, "recipes/recipe_create_form.html", {"form": RecipeForm()})
    
    def post(self, request, *args, **kwargs):
        print(request)
        req_post = request.POST
        new_recipe = Recipe(
            recipe_name = req_post['recipe_name'],
            recipe_desc = req_post['recipe_desc']   
        )

        new_recipe.save()
        return redirect("recipes/")
        
def edit(request, recipe_id):
    pass