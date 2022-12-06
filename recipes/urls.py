from django.urls import path
from . import views

urlpatterns = [ 
    path('index', views.index, name='index'),
    path('<int:id>/', views.recipe_detail, name='recipe details'),
   
]