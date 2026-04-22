from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tên tác phẩm")
    images = models.ImageField(upload_to='products/', verbose_name="Hình ảnh")
    description = models.TextField(verbose_name="Đề tài")
    artist = models.CharField(max_length=100, verbose_name="Tác giả")

    class Meta:
        verbose_name = "Tác phẩm"
        verbose_name_plural = "Tác phẩm"
        
    def __str__(self):
        return self.title

