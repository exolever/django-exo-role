from rest_framework import generics

from .serializers import ExORoleSerializer, CategorySerializer
from ..models import ExORole, Category


class ExORoleListView(generics.ListAPIView):
    queryset = ExORole.objects.all()
    serializer_class = ExORoleSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
