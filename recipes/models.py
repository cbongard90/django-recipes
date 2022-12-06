from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    quantity = models.CharField(max_length=50) 
    unit = models.CharField(max_length=50) 
