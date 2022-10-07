from django.contrib import admin

from .models import ShukatuPost

class CompanyPostAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id', 'title')

admin.site.register(ShukatuPost, CompanyPostAdmin)