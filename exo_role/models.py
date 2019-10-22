from django.db import models

from model_utils.models import TimeStampedModel

from .manager import ExORoleManager
from .conf import settings


class ExORole(TimeStampedModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, choices=settings.EXO_ROLE_CODE_CHOICES, unique=True)
    category = models.CharField(max_length=2, choices=settings.EXO_ROLE_CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)

    objects = ExORoleManager()

    class Meta:
        ordering = ['category', 'name']
        unique_together = ('code', 'category', )

    def __str__(self):
        return self.name
