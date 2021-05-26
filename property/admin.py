from django.contrib import admin

from .models import Flat


class SearchFlat(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owners_phonenumber', ]


admin.site.register(Flat, SearchFlat)
