from django.contrib import admin

from .models import Flat


class SearchFlat(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owners_phonenumber', ]
    readonly_fields = ['created_at']


admin.site.register(Flat, SearchFlat)
