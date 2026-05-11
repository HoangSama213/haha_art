from django.contrib import admin
from classes.models import *

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    
@admin.register(Objects)
class ObjectsAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Programs)
class ProgramsAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['title']
    
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display=['child_name', 'phone', 'area']