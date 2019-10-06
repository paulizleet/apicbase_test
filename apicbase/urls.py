from django.urls import path
#from django.urls import reverse

from . import recipe_views
from . import ingredient_views

app_name = "apicbase"

urlpatterns = [
    path('', recipe_views.IndexView.as_view(), name='recipe-index'),
    path('recipe/', recipe_views.IndexView.as_view(), name='recipe-index'),

    path('recipe/<int:pk>/', recipe_views.DetailView.as_view(), name='recipe-detail'),
    path('recipe/add', recipe_views.RecipeCreate.as_view(), name="new"),
    path('recipe/update/<int:pk>', recipe_views.RecipeUpdate.as_view(), name="update"),

    path('ingredient/', ingredient_views.IndexView.as_view(), name='ingredient-index'),
    path('ingredient/<int:pk>/', ingredient_views.DetailView.as_view(), name='ingredient-detail'),
    path('ingredient/add', ingredient_views.IngredientCreate.as_view(), name="new")
    
]