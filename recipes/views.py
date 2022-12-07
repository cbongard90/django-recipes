from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404

from .models import Recipe, Ingredient, Review
from .forms import RecipeForm

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
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes:index')
    else:
        form = RecipeForm()
    return render(request, 'recipes/new_recipe.html', {'form': form})
