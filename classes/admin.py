from django.contrib import admin
from classes.models import Classes

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']

