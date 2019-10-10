from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

from apicbase.models import Recipe, Ingredient


class SearchView(ListView):

    template_name = "base/search.html" #can use index here because its just a list :)

    def get_queryset(self):
        
        #simple search that finds recipes and ingredients containing any keyword in the query

        search_criteria = self.request.GET["q"]

        #initialize empty querysets
        recipe_results = Recipe.objects.none()
        ingredient_results = Ingredient.objects.none()

        for each in search_criteria.split(" "):
            recipe_results = recipe_results.union(Recipe.objects.filter(name__contains=each))
            ingredient_results = ingredient_results.union(Ingredient.objects.filter(name__contains=each))
            
        return {"recipe_results":recipe_results, "ingredient_results":ingredient_results}

    def get(self, request):
        results = self.get_queryset()
        return render(request, self.template_name, results)
