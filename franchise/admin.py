# admin.py

from django.contrib import admin
from .models import FranchiseHeroImage, FranchiseFormImage


@admin.register(FranchiseHeroImage)
class FranchiseHeroImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'is_active', 'created_at')
    list_editable = ('is_active',)




@admin.register(FranchiseFormImage)
class FranchiseFormImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'is_active', 'created_at')
    list_editable = ('is_active',)