from django.db import models

from model_utils.models import TimeStampedModel

from .manager import ExORoleManager
from .conf import settings


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2, choices=settings.EXO_ROLE_CATEGORY_CODE_CHOICES)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class ExORole(TimeStampedModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, choices=settings.EXO_ROLE_CODE_CHOICES, unique=True)
    categories = models.ManyToManyField('Category', related_name='exo_roles')
    description = models.TextField(blank=True, null=True)

    objects = ExORoleManager()

    class Meta:
        ordering = ['name']
        verbose_name = 'ExORole'
        verbose_name_plural = 'ExORoles'

    def __str__(self):
        return self.name
