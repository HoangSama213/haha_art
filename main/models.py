from django.db import models

class Carousel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel/')
    button1_text = models.CharField(max_length=100, blank=True)
    button1_link = models.CharField(max_length=255, blank=True)
    button2_text = models.CharField(max_length=100, blank=True)
    button2_link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title