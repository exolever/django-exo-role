from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters

from .serializers import ExORoleSerializer
from .filters import ExORoleFilter
from ..models import ExORole


class ExORoleListView(generics.ListAPIView):
    queryset = ExORole.objects.all()
    serializer_class = ExORoleSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filter_class = ExORoleFilter
    ordering = ('name',)
