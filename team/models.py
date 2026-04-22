from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên giáo viên")
    photo = models.ImageField(upload_to='teachers/', verbose_name="Ảnh giáo viên")
    position = models.CharField(max_length=100, verbose_name="Chức danh")
    bio = models.TextField(verbose_name="Tiểu sử")

    class Meta:
        verbose_name = "Giáo viên"
        verbose_name_plural = "Giáo viên"
        
    def __str__(self):
        return self.name