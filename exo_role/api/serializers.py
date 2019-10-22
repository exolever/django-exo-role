from rest_framework import serializers

from ..models import ExORole


class ExORoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExORole
        fields = [
            'name',
            'description',
            'code',
            'category',
            'group_by',
        ]
