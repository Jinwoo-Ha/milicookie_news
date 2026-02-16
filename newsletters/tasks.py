from celery import shared_task
from django.utils import timezone
from django.template.loader import render_to_string
from .models import Newsletter
from subscribers.models import Subscriber
from services.crew_service.crew import DefenseNewsKoreanDailyDigestCrew
from services.email_service import send_newsletter_email
import markdown

@shared_task
def run_newsletter_crew_task():
    """
    Executes the CrewAI process to generate the newsletter content.
    Saves the result to the database and triggers distribution.
    """
    try:
        print("Starting CrewAI task...")
        # Initialize and run the crew
        crew = DefenseNewsKoreanDailyDigestCrew().crew()
        result = crew.kickoff()
        
        # CrewOutput string conversion
        markdown_content = str(result)
        
        # Convert Markdown to HTML for email
        html_content = markdown.markdown(markdown_content)
        
        # Post-process HTML for styling <배경> and <기사>
        # Make them stand out: block display, larger font, bold, margin top/bottom
        style_block = 'style="font-size: 1.4rem; font-weight: 800; color: #1a1a1a; margin-top: 1.5rem; margin-bottom: 0.5rem; display: block;"'
        
        # Style for "Today's Briefing" header
        header_style = 'style="font-size: 1.5rem; font-weight: 800; color: #1a1a1a; margin-bottom: 1rem; border-bottom: 2px solid #1a1a1a; padding-bottom: 0.5rem;"'
        html_content = html_content.replace("# &lt;오늘의 주요 뉴스&gt;", f'<h1 {header_style}>[미리보기]</h1>')
        html_content = html_content.replace("# <오늘의 주요 뉴스>", f'<h1 {header_style}>[미리보기]</h1>')
        html_content = html_content.replace("<h1>&lt;오늘의 주요 뉴스&gt;</h1>", f'<h1 {header_style}>[미리보기]</h1>')

        # 가독성을 위해 문장 끝("다.")마다 줄바꿈 추가
        # 단순히 replace만 하면 의도치 않은 줄바꿈이 생길 수 있으므로 "다. " 패턴을 타겟팅
        html_content = html_content.replace("다.", "다.<br><br>")

        # Create Newsletter entry
        # 한국 시간대(KST) 기준 날짜 가져오기
        today = timezone.now().astimezone(timezone.get_current_timezone()).date()
        
        # 제목 형식 변경: 00월 00일 밀리쿠키 뉴스레터
        title = f"{today.strftime('%m월 %d일')} 밀리쿠키 뉴스레터"
        
        newsletter = Newsletter.objects.create(
            title=title,
            content=html_content, # Store HTML
            summary=markdown_content[:200] + "...", # Simple summary
            published_at=timezone.now()
        )
        
        print(f"Newsletter '{title}' created successfully.")
        
        # Trigger distribution
        distribute_newsletter_task.delay(newsletter.id)
        
        return f"Success: Newsletter {newsletter.id} created."
        
    except Exception as e:
        print(f"Error running CrewAI task: {e}")
        return f"Error: {e}"

@shared_task
def distribute_newsletter_task(newsletter_id):
    """
    Sends the newsletter to all active subscribers.
    """
    try:
        newsletter = Newsletter.objects.get(id=newsletter_id)
        subscribers = Subscriber.objects.filter(is_active=True)
        
        # Prepare email context
        # 한국 시간대(KST) 기준 날짜 가져오기
        current_date_kst = timezone.now().astimezone(timezone.get_current_timezone())
        context = {
            'title': newsletter.title,
            'content': newsletter.content,
            'date': current_date_kst.strftime("%Y. %m. %d / %a"), # e.g. 2026. 02. 14 / Sat
        }
        
        count = 0
        for sub in subscribers:
            # Customize context for each subscriber (e.g., unsubscribe link)
            # In a real app, generate a unique unsubscribe URL
            context['unsubscribe_url'] = "#" 
            
            # Render the HTML email template
            email_body = render_to_string('email_template.html', context)
            
            success = send_newsletter_email(
                recipient_email=sub.email,
                subject=newsletter.title,
                html_content=email_body # Send the rendered template
            )
            if success:
                count += 1
        
        newsletter.sent_count = count
        newsletter.save()
        
        return f"Distributed newsletter {newsletter_id} to {count} subscribers."
    except Newsletter.DoesNotExist:
        return f"Newsletter {newsletter_id} not found."
