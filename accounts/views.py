from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .models import Patient
from .forms import RegisterForm, PatientForm


class HomeView(TemplateView):
    template_name = 'accounts/home.html'

class ContactView(TemplateView):
    template_name = 'accounts/contact.html'

class AboutView(TemplateView):
    template_name = 'accounts/about.html'

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

class UserRegisterView(TemplateView):
    patient_form_class = PatientForm
    register_form_class = RegisterForm
    model = Patient
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def get(self, *args, **kwargs):
        self.init_forms()
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(UserRegisterView, self).get_context_data(**kwargs)
        context['patient_form'] = self.patient_form_class
        context['register_form'] = self.register_form_class
        return context

    def init_forms(self, post_data=None, **kwargs):
        self.patient_form = self.patient_form_class(
            post_data,
            **kwargs
        )
        self.register_form = self.register_form_class(
            post_data,
            **kwargs
        )

    def post(self, request, *args, **kwargs):
        if self.validate_forms():
            self.save_forms()

    def form_valid(self, form):
        valid = super(UserRegisterView, self).form_valid(form)
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        return valid

    def validate_forms(self):
        return all([
            self.patient_form.is_valid(),
            self.register_form.is_valid()
        ])

    def save_forms(self):
        self.patient_form.save()
        self.register_form.save()

