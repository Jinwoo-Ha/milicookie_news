from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True, help_text="User's email address")
    is_active = models.BooleanField(default=True, help_text="Is this subscriber active?")
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-subscribed_at']
