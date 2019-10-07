from django.urls import path
#from django.urls import reverse

from .recipe_views import RecipeIndex, RecipeCreate, RecipeDetail, RecipeUpdate, RecipeSearch
from .ingredient_views import IngredientIndex, IngredientCreate, IngredientDetail, IngredientUpdate, IngredientSearch
from . import recipe_views
from . import ingredient_views

app_name = "apicbase"

urlpatterns = [
    path('', recipe_views.direct_to_index, name='recipe-index'),


    path('recipe/', RecipeIndex.as_view(), name='recipe-index'),
    path('recipe/add', RecipeCreate.as_view(), name="recipe-new"),
    path('recipe/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('recipe/<int:pk>/update', RecipeUpdate.as_view(), name="recipe-update"),
    path('recipe/search', RecipeSearch.as_view(), name="recipe-search"),

    path('ingredient/', IngredientIndex.as_view(), name='ingredient-index'),
    path('ingredient/add', IngredientCreate.as_view(), name="ingredient-new"),
    path('ingredient/<int:pk>/', IngredientDetail.as_view(), name='ingredient-detail'),
    path('ingredient/<int:pk>/update', IngredientUpdate.as_view(), name='ingredient-update'),
    path('ingredient/search', IngredientSearch.as_view(), name='ingredient-search')


    
]