from django.db import models


class BrandStory(models.Model):
    # Header
    label = models.CharField(
        max_length=100,
        default="Hành trình cảm xúc",
        verbose_name="Nhãn nhỏ phía trên tiêu đề"
    )
    title = models.CharField(
        max_length=255,
        default="Câu chuyện thương hiệu",
        verbose_name="Tiêu đề chính"
    )

    # Image
    image = models.ImageField(
        upload_to='brand_story/',
        verbose_name="Ảnh đại diện"
    )
    image_alt = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Mô tả ảnh (alt)"
    )

    # Badge (số năm)
    badge_number = models.CharField(
        max_length=10,
        default="5+",
        verbose_name="Số hiển thị trên badge (vd: 5+)"
    )
    badge_label = models.CharField(
        max_length=50,
        default="Năm tâm huyết",
        verbose_name="Nhãn badge"
    )

    # Intro quote
    intro_text = models.TextField(
        verbose_name="Đoạn giới thiệu (dòng in nghiêng đầu tiên)"
    )
    intro_highlight = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Phần chữ nổi bật trong intro"
    )

    # Closing quote
    closing_quote = models.TextField(
        verbose_name="Câu kết (dòng chữ cam cuối)"
    )

    # Signature
    brand_name = models.CharField(
        max_length=100,
        default="HaHa Art",
        verbose_name="Tên thương hiệu (chữ ký)"
    )
    brand_tagline = models.CharField(
        max_length=255,
        default="Nơi ước mơ được lớn lên 🎨💛",
        verbose_name="Tagline thương hiệu"
    )

    is_active = models.BooleanField(default=True, verbose_name="Hiển thị")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Brand Story"
        verbose_name_plural = "Brand Stories"

    def __str__(self):
        return self.title


class BrandStoryPoint(models.Model):
    """3 điểm nội dung với icon (brush, sentiment_satisfied, menu_book)"""

    ICON_CHOICES = [
        ('brush', 'Brush 🖌️'),
        ('sentiment_satisfied', 'Smile 😊'),
        ('menu_book', 'Book 📖'),
        ('star', 'Star ⭐'),
        ('favorite', 'Favorite ❤️'),
        ('palette', 'Palette 🎨'),
        ('school', 'School 🎓'),
        ('emoji_objects', 'Idea 💡'),
    ]

    COLOR_CHOICES = [
        ('tertiary-container', 'Cam nhạt'),
        ('primary-container', 'Vàng nhạt'),
        ('secondary-fixed', 'Cam đậm nhạt'),
    ]

    brand_story = models.ForeignKey(
        BrandStory,
        on_delete=models.CASCADE,
        related_name='points',
        verbose_name="Brand Story"
    )
    icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='brush',
        verbose_name="Icon (Material Symbol)"
    )
    icon_color = models.CharField(
        max_length=50,
        choices=COLOR_CHOICES,
        default='tertiary-container',
        verbose_name="Màu nền icon"
    )
    content = models.TextField(verbose_name="Nội dung đoạn văn")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="Thứ tự")

    class Meta:
        verbose_name = "Điểm nội dung"
        verbose_name_plural = "Các điểm nội dung"
        ordering = ['order']

    def __str__(self):
        return f"{self.brand_story.title} — Point {self.order}"