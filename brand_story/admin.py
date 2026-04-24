from django.contrib import admin
from .models import BrandStory, BrandStoryPoint


class BrandStoryPointInline(admin.TabularInline):
    model = BrandStoryPoint
    extra = 1
    fields = ('order', 'icon', 'icon_color', 'content')
    ordering = ('order',)


@admin.register(BrandStory)
class BrandStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand_name', 'badge_number', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'brand_name', 'closing_quote')
    list_editable = ('is_active',)

    fieldsets = (
        ('📌 Header', {
            'fields': ('label', 'title')
        }),
        ('🖼️ Hình ảnh', {
            'fields': ('image', 'image_alt')
        }),
        ('🏅 Badge', {
            'fields': ('badge_number', 'badge_label')
        }),
        ('📝 Nội dung', {
            'fields': ('intro_text', 'intro_highlight', 'closing_quote')
        }),
        ('✍️ Chữ ký thương hiệu', {
            'fields': ('brand_name', 'brand_tagline')
        }),
        ('⚙️ Cài đặt', {
            'fields': ('is_active',)
        }),
    )

    inlines = [BrandStoryPointInline]