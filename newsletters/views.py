from django.views.generic import ListView, DetailView
from .models import Newsletter

class NewsletterListView(ListView):
    model = Newsletter
    template_name = 'archive.html'
    context_object_name = 'newsletters'
    ordering = ['-published_at']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        year = self.request.GET.get('year')
        month = self.request.GET.get('month')
        
        if year:
            queryset = queryset.filter(published_at__year=year)
        if month:
            queryset = queryset.filter(published_at__month=month)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all distinct published dates to build the filter options
        dates = Newsletter.objects.dates('published_at', 'month', order='DESC')
        years = sorted(list(set(d.year for d in dates)), reverse=True)
        # We need to pass the current selection back to the template
        context['years'] = years
        context['months'] = range(1, 13)
        context['selected_year'] = self.request.GET.get('year')
        context['selected_month'] = self.request.GET.get('month')
        return context

class NewsletterDetailView(DetailView):
    model = Newsletter
    template_name = 'newsletter_detail.html'
    context_object_name = 'newsletter'
