from django.shortcuts import render, redirect
from django.views import generic

from .models import Ingredient, IngredientForm
from django.http import HttpResponse
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'ingredients/index.html'

    def get_queryset(self):
        return Ingredient.objects.all()[:20]

class DetailView(generic.DetailView):
    model = Ingredient
    template_name = "ingredients/detail.html"

    # def get_absolute_url(self):
    #     ret


class IngredientCreate(generic.edit.CreateView):
    model = Ingredient
    fields = ['ingredient_name', 'ingredient_desc', 'ingredient_cost', 'ingredient_unit_size', 'is_fluid']
    template_name = "ingredients/ingredient_create_page.html"
    

    def get(self, request):
        print("asdf")
        return render(request, "ingredients/ingredient_create_page.html", {"form": IngredientForm()})

    def form_invalid(self, request):
        #do ajax things in here
        # or redirect to the update page and display errors
        return HttpResponse("<html><body>nope</body></html>")


    
    # def post(self, request, *args, **kwargs):
    #     print(request)
    #     req_post = request.POST
    #     new_ingredient = Ingredient(
    #         ingredient_name = req_post['ingredient_name'],
    #         ingredient_desc = req_post['ingredient_desc'],
    #         ingredient_cost = req_post['ingredient_cost'],
    #         ingredient_unit_size = req_post['ingredient_unit_size']
    #     )

    #     if req_post['is_fluid'] == "on":
    #         new_ingredient.is_fluid = True
    #     else:
    #         new_ingredient.is_fluid = False


    #     new_ingredient.save()
    #     return redirect("/")

class IngredientUpdate(generic.edit.UpdateView):

    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredients/ingredient_create_form.html"

    def form_valid(self, form):
        form.save()
        return redirect("/ingredient/%s" % self.kwargs["pk"])
        
#def add_recipe(request, )