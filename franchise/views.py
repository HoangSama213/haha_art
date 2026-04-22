from django.shortcuts import render
from .models import FranchiseHeroImage, FranchiseFormImage


def index(request):
    hero = FranchiseHeroImage.objects.filter(is_active=True).first()
    form_image = FranchiseFormImage.objects.filter(is_active=True).first()
    return render(request, 'franchise.html', {
        'franchise_hero': hero,
        'franchise_form_image': form_image,
    })