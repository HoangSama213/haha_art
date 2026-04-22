# models.py

from django.db import models


class FranchiseHeroImage(models.Model):
    image = models.ImageField(upload_to='franchise/hero/')
    alt_text = models.CharField(max_length=255, default='Sáng tạo cùng trẻ')
    quote = models.CharField(
        max_length=500,
        default='Nơi ươm mầm cho những tài năng nhí tỏa sáng rực rỡ!'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ảnh Hero Nhượng Quyền'
        verbose_name_plural = 'Ảnh Hero Nhượng Quyền'

    def __str__(self):
        return f"Hero Image – {self.alt_text}"
    

class FranchiseFormImage(models.Model):
    image = models.ImageField(upload_to='franchise/form/')
    alt_text = models.CharField(max_length=255, default='Hỗ trợ tận tâm')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ảnh Form Nhượng Quyền'
        verbose_name_plural = 'Ảnh Form Nhượng Quyền'

    def __str__(self):
        return f"Form Image – {self.alt_text}"