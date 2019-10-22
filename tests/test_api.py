from django.test import TestCase

from exo_role.models import ExORole


class TestAPITestCase(TestCase):

    def test_migrations_create_initial_data(self):
        # ASSERTS
        self.assertTrue(ExORole.objects.all().exists())
