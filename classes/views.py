
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from classes.models import Classes, Enrollment


def index(request):
    classes = Classes.objects.all()
    context = {
        'page_title': 'Khóa học',
        'classes': classes,
    }
    return render(request, 'classes/classes.html', context)


def register(request):
    if request.method == 'POST':
        guardian_name = request.POST.get('guardian_name')
        guardian_email = request.POST.get('guardian_email')
        child_name = request.POST.get('child_name')
        child_age = request.POST.get('child_age')
        note = request.POST.get('message', '')

        # Lưu vào database
        enrollment = Enrollment.objects.create(
            guardian_name=guardian_name,
            guardian_email=guardian_email,
            child_name=child_name,
            child_age=child_age,
            message=note,
        )

        # --- Email gửi cho người đăng ký ---
        send_mail(
            subject='Xác nhận đăng ký khóa học',
            message=f"""Xin chào {guardian_name},

Chúng tôi đã nhận được đăng ký tham gia khóa học cho học viên {child_name} ({child_age} tuổi).

Chúng tôi sẽ liên hệ lại với bạn sớm nhất có thể.

Trân trọng,
Đội ngũ hỗ trợ""",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[guardian_email],
            fail_silently=False,
        )

        # --- Email thông báo cho admin ---
        send_mail(
            subject='[Đăng ký mới] ' + child_name,
            message=f"""Có đăng ký mới:

Người giám hộ: {guardian_name}
Email: {guardian_email}
Học viên: {child_name}
Tuổi: {child_age}
Ghi chú: {note}""",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            fail_silently=False,
        )

        messages.success(request, 'Đăng ký thành công! Vui lòng kiểm tra email.')
        return redirect('classes:index')

    return redirect('classes:index')

def detail(request, class_id):
    try:
        class_obj = Classes.objects.get(id=class_id)
    except Classes.DoesNotExist:
        messages.error(request, 'Lớp học không tồn tại.')
        return redirect('classes:index')

    context = {
        'page_title': class_obj.title,
        'class': class_obj,
    }
    return render(request, 'classes/classes_detail.html', context)