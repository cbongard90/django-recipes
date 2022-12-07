from django.contrib import admin

# Register your models here.
from .models import Recipe
from .models import Ingredient
from .models import Review

class recipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'instructions', 'prep_time', 'cook_time', 'photo', 'timestamp')

admin.site.register(Recipe, recipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Review)
