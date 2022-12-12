from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    prep_time = models.CharField(max_length=50, blank=True, null=True)
    cook_time = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to='recipe_photos', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredientName = models.CharField(max_length=220)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return self.ingredientName

class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    title = models.CharField(max_length=220)
    comment = models.TextField(blank=True, null=True)
    rating = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
