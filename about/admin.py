from django.contrib import admin

from about.models import *

# Register your models here.
@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['title']
    
@admin.register(Different)
class DifferentAdmin(admin.ModelAdmin):
    list_display = ['title']
    
@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Promote)
class PromoteAdmin(admin.ModelAdmin):
    list_display = ['title']