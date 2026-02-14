from django.db import models

class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(help_text="Full HTML content of the newsletter")
    summary = models.TextField(blank=True, help_text="Short summary for the archive list")
    published_at = models.DateTimeField(auto_now_add=True)
    sent_count = models.IntegerField(default=0, help_text="Number of subscribers this was sent to")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']
