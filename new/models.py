from django.db import models

# Create your models here.
class News_Type(models.Model):
    title = models.CharField(max_length=200, verbose_name='Loại tin tức')  # Tiêu đề tin tức

    class Meta:
        verbose_name = 'Loại tin tức'
        verbose_name_plural = 'Loại tin tức'
        
    def __str__(self):
        return self.title
    
class News(models.Model):
    news_type = models.ForeignKey(News_Type, on_delete=models.CASCADE, verbose_name='Loại tin tức')  # Liên kết với loại tin tức
    title = models.CharField(max_length=200, verbose_name='Tiêu đề')  # Tiêu đề tin tức
    content_1 = models.TextField(verbose_name='Nội dung 1',blank=True)  # Nội dung chi tiết của tin tức
    content_2 = models.TextField(verbose_name='Nội dung 2', blank=True)  # Nội dung chi tiết của tin tức
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Ngày đăng')  # Ngày đăng tin tức
    images_1 = models.ImageField(upload_to='class_news/', verbose_name='Hình ảnh 1', blank=True, null=True)  # Hình ảnh liên quan đến tin tức
    images_2 = models.ImageField(upload_to='class_news/', verbose_name='Hình ảnh 2', blank=True, null=True)  # Hình ảnh liên quan đến tin tức
    images_3 = models.ImageField(upload_to='class_news/', verbose_name='Hình ảnh 3', blank=True, null=True)  # Hình ảnh liên quan đến tin tức
    
    class Meta:
        verbose_name = 'Bảng tin'
        verbose_name_plural = 'Bảng tin'
        
    def __str__(self):
        return self.title + ' - ' + str(self.created_at)
    
