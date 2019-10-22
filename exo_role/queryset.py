from django.db.models import QuerySet


class ExORoleQueryset(QuerySet):

    def filter_by_code(self, code):
        return self.filter(code=code)

    def filter_by_category(self, category):
        return self.filter(categories__in=[category])
