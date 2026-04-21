from django.db import models

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


class TrainingPolicy(models.Model):
    title = models.CharField(max_length=200, default="Quy chế đào tạo")
    content = models.TextField()
    image = models.ImageField(upload_to='policy/')

    class Meta:
        verbose_name = "Quy chế đào tạo"
        verbose_name_plural = "Quy chế đào tạo"

    def __str__(self):
        return self.title