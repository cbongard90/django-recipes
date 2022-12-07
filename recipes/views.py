from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Recipe, Ingredient, Review

# Create your views here.
def index(request):
    recipe_list = Recipe.objects.all()
    context = {
        'recipe_list' : recipe_list,
    }
    return render(request, 'recipes/index.html', context)


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def add_review(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    try:
        rating = int(request.POST['rating'])
        comment = request.POST['comment']
    except (KeyError, ValueError):
        return render(request, 'recipes/recipe_detail.html', {
            'recipe': recipe,
            'error_message': "You didn't provide a rating or a comment",
        })
    else:
        Review.objects.create(recipe=recipe, rating=rating, comment=comment)
        return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def new_recipe(request):
    context = {}

    return render(request, 'recipes/new_recipe.html', context)

def create_recipe(request):
    recipe = Recipe.objects.create(
        name=request.POST['name'],
        description=request.POST['description'],
        instructions=request.POST['instructions'],
        cook_time=request.POST['cook_time'],
        servings=request.POST['servings'],
        source=request.POST['source'],
        source_url=request.POST['source_url'],
        image_url=request.POST['image_url']
    )
    for ingredient in request.POST.getlist('ingredients'):
        Ingredient.objects.create(recipe=recipe, name=ingredient)

    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
