from django.urls import path, include, reverse_lazy
from .forms import RegistrationForm

from django.views.generic.edit import CreateView

urlpatterns = [
    path('profile/', include('django.contrib.auth.urls')),
    path(
        'registration/',
        CreateView.as_view(
            template_name="registration/registration_form.html",
            form_class=RegistrationForm,
            success_url=reverse_lazy('homepage:index')
        ),
        name='registration'
    )
]
