from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name="Tên")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=255, verbose_name="Tiêu đề")
    message = models.TextField(verbose_name="Nội dung")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Liên hệ"
        verbose_name_plural = "Liên hệ"

    def __str__(self):
        return f"{self.name} - {self.subject}"