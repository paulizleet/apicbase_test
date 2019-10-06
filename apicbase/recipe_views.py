from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from .models import Recipe, RecipeForm


# Create your views here.

###############################################
#using generic class views because....??????
###############################################
# felt like having a bunch of methods named recipe_index, recipe_get_create, recipe_post_create etc
# was cumbersome.  generic views have methods to override (or not) to get the functionality I desire

class IndexView(generic.ListView):
    template_name = 'recipes/index.html'

    def get_queryset(self):
        return Recipe.objects.all()[:20]
        

class DetailView(generic.DetailView):
    
    model = Recipe
    template_name = "recipes/detail.html"

    def get(self, request, pk):
        
        recipe = Recipe.objects.get(id=pk)
        display_data = recipe.assemble_for_display()

        return render(request, "recipes/detail.html", {'recipe': recipe, 'data': display_data[0], 'cost': display_data[1]})
        #somewhere areound here is where you pull data together to pass into the templates



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
        return redirect("/")

class RecipeUpdate(generic.edit.UpdateView):
    model = Recipe
    
    # def get(self, request):
    #     print("asdf")
    #     return render(request, "recipes/recipe_create_form.html", {"form": RecipeForm()})
    
    # def post(self, request, *args, **kwargs):
    #     print(request)
    #     req_post = request.POST
    #     new_recipe = Recipe(
    #         recipe_name = req_post['recipe_name'],
    #         recipe_desc = req_post['recipe_desc']  
    #     )

    #     new_recipe.save()
    #     return redirect("/")
def direct_to_index(request):
    print("gotcha")
    return redirect("/recipe")