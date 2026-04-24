from django.shortcuts import render
from .models import BrandStory


def brand_story(request):
    story = BrandStory.objects.filter(is_active=True).prefetch_related('points').first()
    return render(request, 'brand_story/brand_story.html', {'story': story})