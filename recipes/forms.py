from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'instructions', 'prep_time', 'cook_time', 'photo')
