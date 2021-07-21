from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    return render(request, 'home/index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')

        data = {
            'name': name,
            'email': email,
            'phone': phone,
            'content': content
        }

        send_mail(
            data['name'],
            'Name: '
            + data['name']
            + '\nEmail: '
            + data['email']
            + '\nMobile: '
            + data['phone']
            + '\n\nMessage:\n'
            + data['content'],
            'happyus404@gmail.com',
            ['happyus404@gmail.com'],
            fail_silently=False
        )

        return render(request, 'home/thank-you.html')
    else:
        return render(request, 'home/contact.html')
