from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


# Entry point per l'applicazione single page
class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"