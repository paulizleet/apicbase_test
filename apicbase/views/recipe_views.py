from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from apicbase.models import Recipe, RecipeForm
from django.core.paginator import Paginator

# Felt like having a bunch of methods named recipe_index, recipe_get_create, recipe_post_create etc
# was cumbersome.  generic views have methods to override (or not) to get the functionality I desire

class RecipeIndex(ListView):
    template_name = 'recipes/index.html'
    def get(self, request):
        recipe_list = Recipe.objects.all()
        paginator = Paginator(recipe_list, 20)
        page_num = 0
        page_num = request.GET.get("page")
        recipes = paginator.get_page(page_num)
        # pass in page_nums so I can iteratively make page number links
        return render(request, self.template_name, {'recipes': recipes, 'page_nums': range(1, paginator.num_pages+1)})


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

        form = RecipeForm()
        print("asdf")
        return render(request, "recipes/recipe_create_form.html", {"form": RecipeForm()})
    
    def post(self, request, *args, **kwargs):
        req_post = request.POST
        new_recipe = Recipe(
            name = req_post['name'],
            desc = req_post['desc']  
        )

        new_recipe.save()

        # Parse ingredients
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
        recipe = Recipe.objects.get(id=kwargs["pk"])

        for each in recipe.ingredients.all():
            each.delete()
        ingredient_string = request.POST["ingredients"]
        recipe.add_ingredients(ingredient_string)


        #return rendered template instead of whole page
        return redirect(recipe) 

def direct_to_index(request):
    return redirect("/recipe")