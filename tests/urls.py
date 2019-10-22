from django.urls import path, include

app_name = 'exo-role'

urlpatterns = [
    path('api/', include('exo_role.api.urls')),
]
