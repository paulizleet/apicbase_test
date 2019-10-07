from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from .models import Recipe, RecipeForm


# Create your views here.

###############################################
#using generic class views because....??????
###############################################
# felt like having a bunch of methods named recipe_index, recipe_get_create, recipe_post_create etc
# was cumbersome.  generic views have methods to override (or not) to get the functionality I desire

class RecipeIndex(ListView):
    template_name = 'recipes/index.html'
    paginate_by = 20
    def get_queryset(self):
        return Recipe.objects.all()#[:20]
        

class RecipeDetail(DetailView):
    
    model = Recipe
    template_name = "recipes/detail.html"

    def get(self, request, pk):
        recipe = Recipe.objects.get(id=pk)
        display_data = recipe.assemble_for_display()
        return render(request, self.template_name, {'recipe': recipe, 'data': display_data[0], 'cost': display_data[1]})



class RecipeCreate(CreateView):
    model = Recipe
    
    def get(self, request):
        print("asdf")
        return render(request, "recipes/recipe_create_form.html", {"form": RecipeForm()})
    
    def post(self, request, *args, **kwargs):
        req_post = request.POST
        new_recipe = Recipe(
            recipe_name = req_post['recipe_name'],
            recipe_desc = req_post['recipe_desc']  
        )
        new_recipe.save()

        # parse ingredients
        new_recipe.add_ingredients(req_post["ingredients"])
  
        return redirect(new_recipe)

class RecipeUpdate(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/recipe_create_form.html"

    def form_valid(self, form):
        print("asdf")
        return redirect("/recipe/%s" % self.kwargs["pk"])

    def post(self, request, *args, **kwargs):
        # This is jank but I don't know what questions to ask to do it the right way
        print("asdf")
        recipe = Recipe.objects.get(id=kwargs["pk"])

        for each in recipe.ingredients.all():
            each.delete()
        ingredient_string = request.POST["ingredients"]
        recipe.add_ingredients(ingredient_string)

        return redirect(recipe)

class RecipeSearch(ListView):
    model = Recipe

    # Change this later!
    tamplate_name = "recipe/index.html" #can use index here because its just a list :)
    
    def get(self, request):
        for each in search_criteria.split(" "):
            results = Recipe.objects.filter(recipe_name__contains=each)

def direct_to_index(request):
    print("gotcha")
    print(request)
    return redirect("/recipe")