from django.contrib import admin
from .models import TrainingPolicy


@admin.register(TrainingPolicy)
class TrainingPolicyAdmin(admin.ModelAdmin):
    list_display = ['title']