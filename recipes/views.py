from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views.decorators import csrf

from .models import Recipe, Ingredient, Review
from .forms import RecipeForm, IngredientForm

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
    if request.method == 'POST':
        formRecipe = RecipeForm(request.POST, request.FILES)
        formIngredient = IngredientForm(request.POST)

        if formRecipe.is_valid() and formIngredient.is_valid():
            recipe = formRecipe.save()
            ingredient = formIngredient.save(False)
            ingredient.recipe = recipe
            ingredient.save()
            return redirect('recipes:index')
    else:
        formRecipe = RecipeForm()
        formIngredient = IngredientForm()
    args = {}
    args['formRecipe'] = formRecipe
    args['formIngredient'] = formIngredient
    return render(request, 'recipes/new_recipe.html', args)
