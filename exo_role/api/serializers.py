from rest_framework import serializers

from ..models import ExORole, Category


class CategoryExORoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExORole
        fields = [
            'name',
            'code',
            'description',
        ]


class CategorySerializer(serializers.ModelSerializer):
    exo_roles = CategoryExORoleSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            'name',
            'code',
            'description',
            'exo_roles',
        ]


class ExORoleCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'name',
            'code',
            'description',
        ]


class ExORoleSerializer(serializers.ModelSerializer):
    categories = ExORoleCategorySerializer(many=True)

    class Meta:
        model = ExORole
        fields = [
            'name',
            'description',
            'code',
            'categories',
        ]
