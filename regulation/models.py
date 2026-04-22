from django.db import models

# Create your models here.
class TrainingPolicy(models.Model):
    title = models.CharField(max_length=200, default="Quy chế đào tạo")
    content = models.TextField()
    image = models.ImageField(upload_to='policy/')

    class Meta:
        verbose_name = "Quy chế đào tạo"
        verbose_name_plural = "Quy chế đào tạo"

    def __str__(self):
        return self.title