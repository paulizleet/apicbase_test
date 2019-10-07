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
        req_post = request.POST
        new_recipe = Recipe(
            recipe_name = req_post['recipe_name'],
            recipe_desc = req_post['recipe_desc']  
        )


        new_recipe.save()
        # parse ingredients
        for each in req_post["ingredients"].split(";"):

            #  each looks something like "123,987"
            #  split[0] is the ingredient id
            #  split[1] is the quantity
            

            try:
                splits = each.split(",")
                new_recipe.add_ingredient(ing=splits[0], quantity=splits[1])
            except IndexError:
                #  since these strings will always end with a trailing ';', 
                #  it will cause an exception when the final split piece is ''
                #  we don't need the loop anymore so we jump out of it
                break

        return redirect(new_recipe)

class RecipeUpdate(generic.edit.UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/recipe_create_form.html"

    #going to jam the selector in via jquery

    # def get(self, request, pk):
    #     recipe = self.get_object()
    #     recipe_ingredients = recipe.ingredients.all
    #     form = self.get_form()

    #     return render(request, self.template_name, {"form": self.form_class, "recipe": recipe, "recipe_ingredients": recipe_ingredients})
    def form_invalid(self, form):
        print("asdf")

    def form_valid(self, form):
        print("asdf")
        return redirect("/recipe/%s" % self.kwargs["pk"])

    def post(self, request, form):
        print("asdf")
    

def direct_to_index(request):
    print("gotcha")
    print(request)
    return redirect("/recipe")