from django.views.generic import CreateView, TemplateView
from pages.form import ContactModelForm
import logging

logger = logging.getLogger(__name__)

class HomePageView(TemplateView):
    template_name = 'home.html'

class ContactTemplateView(TemplateView):
    template_name = 'contact.html'
    form_class = ContactModelForm
    success_url = '/'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        logger.debug("Form instantiated: %s", form)
        return form
