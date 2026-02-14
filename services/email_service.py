
import os
import resend
from django.conf import settings

def send_newsletter_email(recipient_email, subject, html_content):
    """
    Sends an email using Resend API.
    """
    if not os.environ.get("RESEND_API_KEY"):
        print("RESEND_API_KEY is not set. Skipping email sending.")
        return False
        
    resend.api_key = os.environ.get("RESEND_API_KEY")

    try:
        r = resend.Emails.send({
            "from": "newsletter@milicookie.cloud", # Sandbox default, needs verification for production
            "to": recipient_email,
            "subject": subject,
            "html": html_content,
        })
        print(f"Email sent to {recipient_email}: {r}")
        return True
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")
        return False
