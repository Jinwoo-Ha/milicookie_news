from django.views.generic import ListView, DetailView
from .models import Newsletter

class NewsletterListView(ListView):
    model = Newsletter
    template_name = 'archive.html'
    context_object_name = 'newsletters'
    ordering = ['-published_at']
    paginate_by = 10

class NewsletterDetailView(DetailView):
    model = Newsletter
    template_name = 'newsletter_detail.html'
    context_object_name = 'newsletter'
