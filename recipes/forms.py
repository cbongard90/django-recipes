from django import forms
from django.forms import formset_factory
from .models import Recipe, Ingredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'instructions', 'prep_time', 'cook_time', 'photo')

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('ingredientName', 'quantity')
        labels = {
            'ingredientName': 'Name',
        }

ingredientFormSet = formset_factory(IngredientForm, extra=1)
