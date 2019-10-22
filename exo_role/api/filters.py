import django_filters

from django.db.models import Q

from ..models import ExORole


class ExORoleFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(method='filter_category')

    def get_filter_values(self, value):
        values_array = value.split(',')
        return [item for item in values_array if item]

    def filter_category(self, queryset, name, value):
        query = Q()
        values = self.get_filter_values(value)

        for value in values:
            query |= Q(category__icontains=value)

        return queryset.filter(query)

    class Meta:
        model = ExORole
        fields = ['code', 'category']
