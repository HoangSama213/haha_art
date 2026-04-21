from django.contrib import admin
from .models import AboutSection, TrainingPolicy

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(TrainingPolicy)
class TrainingPolicyAdmin(admin.ModelAdmin):
    list_display = ['title']