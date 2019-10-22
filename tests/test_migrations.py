from django.test import TestCase

from exo_role.models import ExORole, Category


class TestMigrationsTestCase(TestCase):

    def test_migrations_create_initial_roles(self):
        # PREPARE DATA
        categories = Category.objects.all()

        # ASSERTS
        for category in categories:
            self.assertTrue(ExORole.objects.all().filter_by_category(category).exists())
