from django.urls import path
#from django.urls import reverse

from .recipe_views import RecipeIndex, RecipeCreate, RecipeDetail, RecipeUpdate
from .ingredient_views import IngredientIndex, IngredientCreate, IngredientDetail, IngredientUpdate
from . import recipe_views
from . import ingredient_views
from .misc_views import SearchView

app_name = "apicbase"

urlpatterns = [
    path('', recipe_views.direct_to_index, name='recipe-index'),
    path('search/', SearchView.as_view(), name="search-results"),


    path('recipe/', RecipeIndex.as_view(), name='recipe-index'),
    path('recipe/add', RecipeCreate.as_view(), name="recipe-new"),
    path('recipe/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('recipe/<int:pk>/update', RecipeUpdate.as_view(), name="recipe-update"),

    path('ingredient/', IngredientIndex.as_view(), name='ingredient-index'),
    path('ingredient/add', IngredientCreate.as_view(), name="ingredient-new"),
    path('ingredient/<int:pk>/', IngredientDetail.as_view(), name='ingredient-detail'),
    path('ingredient/<int:pk>/update', IngredientUpdate.as_view(), name='ingredient-update'),


    
]