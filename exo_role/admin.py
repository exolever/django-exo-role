from django.contrib import admin

from .models import ExORole


@admin.register(ExORole)
class ExORoleAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    list_display = ('name', 'category', 'code', 'description')
