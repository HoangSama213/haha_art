from django.contrib import admin

from about.models import AboutSection

# Register your models here.
@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['title']