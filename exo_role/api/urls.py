from django.conf.urls import url

from .views import ExORoleListView

app_name = 'exo-role'

urlpatterns = [
    url(r'^$', ExORoleListView.as_view(), name='list'),
]
