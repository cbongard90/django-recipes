from django.urls import path
from . import views

app_name = 'recipes'
urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),

]
