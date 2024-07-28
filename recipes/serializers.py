from rest_framework import serializers
from .models import Unit, Ingredient, IngredientQuantity, DietaryRestriction, Recipe

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['symbol']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']

class IngredientQuantitySerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()
    unit = UnitSerializer()

    class Meta:
        model = IngredientQuantity
        fields = ['quantity', 'ingredient', 'unit']

class DietaryRestrictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietaryRestriction
        fields = ['name']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.SerializerMethodField()
    dietary_restrictions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'dietary_restrictions']

    def get_ingredients(self, obj):
        # Retrieve IngredientQuantity objects related to the recipe
        ingredient_quantities = obj.ingredients.all()
        # Format each ingredient quantity into a readable string
        return [
            f"{iq.quantity} {iq.unit.symbol} of {iq.ingredient.name}"
            for iq in ingredient_quantities
        ]