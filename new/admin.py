from django.contrib import admin

from new.models import *

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['news_type','title', 'created_at']
    
admin.site.register(News_Type)
