import factory

from django.conf import settings

from factory import django

from utils.faker_factory import faker

from .models import ExORole


class FakeExORoleFactory(django.DjangoModelFactory):

    class Meta:
        model = ExORole

    name = faker.word()
    description = faker.text()
    code = factory.fuzzy.FuzzyChoice(dict(settings.EXO_ROLES_CHOICES).keys())
    category = factory.fuzzy.FuzzyChoice(dict(settings.EXO_ROLE_CH_TYPE).keys())
