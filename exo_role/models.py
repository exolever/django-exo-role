from django.db import models
from django.conf import settings as settings_global

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

    @property
    def is_job(self):
        return self.code in settings.EXO_ROLES_PROJECT_WITH_JOBS

    @property
    def is_manager(self):
        return self.code in [
            settings_global.ROL_CH_HEAD_COACH,
            settings_global.ROL_CH_CURATOR,
            settings_global.ROL_CH_CO_CURATOR,
        ]

    @property
    def group_by(self):
        group_by = None

        roles = [
            settings_global.ROL_CH_TRAINER,
            settings_global.ROL_CH_ALIGN_TRAINER,
        ]

        if self.code in roles:
            group_by = settings_global.ROL_CH_EXO_TRAINER

        return group_by
