from django.db import models

# Create your models here.
# primary key
class Recipe(models.Model):
    title = models.CharField(max_length=250)
    ingredients = models.JSONField()

    def __str__(self):
        return self.title

#foreign key that belongs to a primary key
class Allergen(models.Model):
    allergen = models.CharField(max_length=200)

    def __str__(self):
        return self.allergen
    

