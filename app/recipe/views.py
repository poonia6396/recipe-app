"""
Views for the recipe API.
"""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from recipe.serializers import RecipeSerializer

from core.models import Recipe

class RecipeViewSet(viewsets.ModelViewSet):
    """"""
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """"""
        return Recipe.objects.filter(user=self.request.user).order_by('-id')

