from django.test import TestCase
from django.conf import settings

from exo_role.models import ExORole


class TestMigrationsTestCase(TestCase):

    def test_migrations_create_initial_roles(self):
        # PREPARE DATA
        categories = dict(settings.EXO_ROLE_CATEGORY_CHOICES).keys()

        # ASSERTS
        for category in categories:
            self.assertTrue(ExORole.objects.all().filter_by_category(category).exists())
