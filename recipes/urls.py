from django.urls import path
from . import views

app_name = 'recipes'
urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/review', views.add_review, name='add_review'),
    path('recipe/new/', views.new_recipe, name='new_recipe'),
    path('recipe/create/', views.create_recipe, name='create_recipe')
]
