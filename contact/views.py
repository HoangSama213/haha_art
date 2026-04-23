from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Contact

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message', '')

        # Lưu vào database
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        # Email xác nhận gửi cho người liên hệ
        send_mail(
            subject=f'Xác nhận: {subject}',
            message=f"""Xin chào {name},

Chúng tôi đã nhận được tin nhắn của bạn và sẽ phản hồi sớm nhất có thể.

Nội dung bạn gửi:
{message}

Trân trọng,
Đội ngũ hỗ trợ""",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        # Email thông báo cho admin
        send_mail(
            subject=f'[Liên hệ mới] {subject}',
            message=f"""Có liên hệ mới:

Tên: {name}
Email: {email}
Tiêu đề: {subject}
Nội dung: {message}""",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            fail_silently=False,
        )

        messages.success(request, 'Gửi tin nhắn thành công! Chúng tôi sẽ liên hệ lại sớm.')
        return redirect('contact:contact')

    return render(request, 'contact/contact.html')