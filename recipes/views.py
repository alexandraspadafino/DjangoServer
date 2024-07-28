from rest_framework import viewsets
from .models import Recipe
from .serializers import RecipeSerializer

# Create your views here.
# request -> response 
# request handler
# action

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

