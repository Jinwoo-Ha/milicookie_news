"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))dfd
"""

from django.contrib import admin
from django.urls import path
from subscribers.views import home, subscribe, research
from newsletters.views import NewsletterListView, NewsletterDetailView
from dashboard.views import dashboard_view, trigger_crew

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('research/', research, name='research'),
    path('subscribe/', subscribe, name='subscribe'),
    path('archive/', NewsletterListView.as_view(), name='archive'),
    path('archive/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_detail'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard/trigger/', trigger_crew, name='trigger_crew'),
]
