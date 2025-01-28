from django.urls import path
from. import views

urlpatterns = [
    path('recipe_list', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipe_detail', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe_create', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('ingredient_create/', views.IngredientCreateView.as_view(), name='ingredient_create'),

]