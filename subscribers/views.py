from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscriber

def home(request):
    return render(request, 'home.html')

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if Subscriber.objects.filter(email=email).exists():
                messages.warning(request, '이미 구독한 이메일이에요!')
            else:
                Subscriber.objects.create(email=email)
                messages.success(request, '구독이 완료되었습니다!')
        else:
            messages.error(request, '유효한 이메일 주소를 입력해주세요.')
    return redirect('home')
