from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

# Create your views here.
def index(request):
    recipe_list = Recipe.objects.all()
    context = {
        'recipe_list' : recipe_list,
    }
    return render(request, 'index.html', context)


def recipe_detail(request, id):
    return HttpResponse("You're looking at the recipe %s." %id)