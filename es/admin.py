from django.contrib import admin
from .models import EsPost

class EsPostAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id', 'title')

admin.site.register(EsPost, EsPostAdmin)