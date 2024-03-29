from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from django.urls import reverse_lazy


from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("signup")
    template_name = "signup.html"


