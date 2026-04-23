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

    class Meta:
        verbose_name = "Khóa học"
        verbose_name_plural = "Khóa học"

    def __str__(self):
        return self.title

from django.db import models

class Enrollment(models.Model):
    guardian_name = models.CharField(max_length=255, verbose_name="Tên người giám hộ")
    guardian_email = models.EmailField(verbose_name="Email người giám hộ")
    child_name = models.CharField(max_length=255, verbose_name="Tên học viên")
    child_age = models.CharField(max_length=50, verbose_name="Tuổi học viên")
    message = models.TextField(blank=True, verbose_name="Ghi chú")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Đăng ký"
        verbose_name_plural = "Đăng ký"

    def __str__(self):
        return f"{self.child_name} - {self.guardian_name}"