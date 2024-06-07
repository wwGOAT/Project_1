from typing import Any
from django.views.generic import TemplateView
from .models import FedbackModelPage


class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fedbacks"] = FedbackModelPage.objects.all()
        
        return context