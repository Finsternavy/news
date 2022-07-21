from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    from_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "register/signup.html"

