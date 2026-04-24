from django.shortcuts import render
from django.core.paginator import Paginator
from new.models import *

# Create your views here.
def index(request):
    news = News.objects.all().order_by('-created_at')  # Lấy tất cả tin tức, sắp xếp theo ngày đăng mới nhất
    # 1. Lấy tất cả các loại tin để hiển thị ở Sidebar
    news_type = News_Type.objects.all()
    news_id = request.GET.get('type')
    # Lấy ID loại tin từ URL (ví dụ: ?news_id=1)
    if news_id:
        news = news.filter(news_type__title=news_id)
    paginator = Paginator(news, 4)  # Hiển thị 4 tin tức mỗi trang
    # Lấy số trang hiện tại từ URL (ví dụ: ?page=2)
    page_number = request.GET.get('page') 
    # Lấy các bài viết của trang đó
    page_obj = paginator.get_page(page_number)
    
    context = {
        'news': page_obj,
        'page_obj': page_obj,  # Truyền đối tượng trang vào context
        'page_title': 'Bảng tin HAHA ART',  # Thêm tiêu đề trang vào context
        'news_type': news_type,  # Truyền danh sách loại tin vào context
        'current_type': news_id,  # Truyền ID loại tin hiện tại vào context
    }
    return render(request, 'new/new.html', context)

def detail(request, news_id):
    news = News.objects.get(id=news_id)
    related_news = News.objects.filter(
        news_type=news.news_type
    ).exclude(pk=news.id).order_by('-created_at')[:5]
    context = {
        'news': news,
        'related_news': related_news,
        'page_title': "Tin tức",  # Sử dụng tiêu đề của tin tức làm tiêu đề trang
    }
    return render(request, 'new/new_detail.html', context)