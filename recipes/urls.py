from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
# URL conf module
urlpatterns = [
    path('', include(router.urls)), 
]