from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Ingredient, IngredientForm
from django.http import HttpResponse
# Create your views here.

class IngredientIndex(ListView):
    template_name = 'ingredients/index.html'

    def get_queryset(self):
        return Ingredient.objects.all()[:20]

class IngredientDetail(DetailView):
    model = Ingredient
    template_name = "ingredients/detail.html"


class IngredientCreate(CreateView):
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


class IngredientUpdate(UpdateView):

    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredients/ingredient_create_form.html"

    def form_valid(self, form):
        form.save()
        return redirect("/ingredient/%s" % self.kwargs["pk"])

class IngredientSearch(ListView):
    pass
        
#def add_recipe(request, )