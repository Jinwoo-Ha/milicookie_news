from celery import shared_task
from django.utils import timezone
from .models import Newsletter
from subscribers.models import Subscriber
from services.crew_service.crew import DefenseNewsKoreanDailyDigestCrew
from services.email_service import send_newsletter_email
from django.template.loader import render_to_string
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
        
        # Create Newsletter entry
        today = timezone.now().date()
        title = f"방산 뉴스 데일리 다이제스트 - {today}"
        
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
        
        # Render the full email template with the newsletter content
        full_email_html = render_to_string('emails/newsletter.html', {'newsletter': newsletter})
        
        count = 0
        for sub in subscribers:
            success = send_newsletter_email(
                recipient_email=sub.email,
                subject=newsletter.title,
                html_content=full_email_html
            )
            if success:
                count += 1
        
        newsletter.sent_count = count
        newsletter.save()
        
        return f"Distributed newsletter {newsletter_id} to {count} subscribers."
    except Newsletter.DoesNotExist:
        return f"Newsletter {newsletter_id} not found."
