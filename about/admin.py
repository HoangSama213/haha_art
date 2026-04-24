from django.contrib import admin

from about.models import AboutSection, Different

# Register your models here.
@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['title']
    
@admin.register(Different)
class DifferentAdmin(admin.ModelAdmin):
    list_display = ['title']