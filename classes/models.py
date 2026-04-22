from django.db import models

# Create your models here.
class Classes(models.Model):
    title = models.CharField(max_length=255,verbose_name="Tên khóa học")
    teacher = models.ForeignKey('team.Teacher', on_delete=models.CASCADE, null=True, verbose_name="Giáo viên")
    age = models.CharField(max_length=100, verbose_name="Độ tuổi")
    time= models.CharField(max_length=100, verbose_name="Thời gian học")
    quantity = models.IntegerField(verbose_name="Số lượng học viên")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Giá")
    image = models.ImageField(upload_to='classes/',verbose_name="Ảnh khóa học")

    def __str__(self):
        return self.title