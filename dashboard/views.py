from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from subscribers.models import Subscriber
from newsletters.models import Newsletter
from newsletters.tasks import run_newsletter_crew_task

@staff_member_required
def dashboard_view(request):
    total_subscribers = Subscriber.objects.count()
    total_newsletters = Newsletter.objects.count()
    recent_subscribers = Subscriber.objects.all().order_by('-subscribed_at')[:10]
    
    context = {
        'total_subscribers': total_subscribers,
        'total_newsletters': total_newsletters,
        'recent_subscribers': recent_subscribers,
    }
    return render(request, 'admin_custom.html', context)

@staff_member_required
def trigger_crew(request):
    if request.method == 'POST':
        # Trigger Celery Task
        run_newsletter_crew_task.delay()
        messages.success(request, '뉴스레터 생성 작업이 백그라운드에서 시작되었습니다. 완료까지 시간이 소요됩니다.')
    return redirect('dashboard')
