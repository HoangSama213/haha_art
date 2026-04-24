from django.db import models

# Create your models here.
class AboutSection(models.Model):
    title = models.CharField(max_length=200, default="Giới thiệu về HaHa Art")
    desc_1 = models.TextField(blank=True)
    desc_2 = models.TextField(blank=True)
    desc_3 = models.TextField(blank=True)
    desc_4 = models.TextField(blank=True)
    desc_5 = models.TextField(blank=True)
    image_1 = models.ImageField(upload_to='about/', blank=True)  # ảnh to ở trên
    image_2 = models.ImageField(upload_to='about/', blank=True)  # ảnh trái dưới
    image_3 = models.ImageField(upload_to='about/', blank=True)  # ảnh phải dưới

    class Meta:
        verbose_name = "Giới thiệu"
        verbose_name_plural = "Giới thiệu"

    def __str__(self):
        return self.title

class Different(models.Model):
    title = models.CharField(max_length=200, default="Điểm khác biệt của HaHa Art")
    desc_1 = models.TextField(blank=True,verbose_name="Nội dung")
    image_1 = models.ImageField(upload_to='about/different/',verbose_name="Ảnh minh họa") 

    class Meta:
        verbose_name = "Điểm khác biệt"
        verbose_name_plural = "Điểm khác biệt"

    def __str__(self):
        return self.title
