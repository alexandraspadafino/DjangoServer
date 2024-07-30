from django.contrib import admin
from .models import Recipe, DietaryRestriction, Ingredient, IngredientQuantity, Unit
# Register your models here.

admin.site.register(DietaryRestriction)
admin.site.register(Unit)
admin.site.register(Ingredient)
admin.site.register(IngredientQuantity)
admin.site.register(Recipe)