from django.db import models

# Create your models here.
class DietaryRestriction(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Unit(models.Model):
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.symbol
    
class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    units = models.ManyToManyField(Unit, through='IngredientQuantity')

    def __str__(self):
        return self.name
    
class IngredientQuantity(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=25)  # Or DecimalField depending on your needs

    def __str__(self):
        return f"{self.quantity} {self.unit.symbol} of {self.ingredient.name}"

    
# primary key
class Recipe(models.Model):
    title = models.CharField(max_length=250)
    ingredients = models.ManyToManyField(IngredientQuantity, blank=True)
    Dietary_Restrictions = models.ManyToManyField(DietaryRestriction, blank=True)

    def __str__(self):
        return self.title
    

