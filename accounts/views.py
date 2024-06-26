from pyexpat.errors import messages

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .models import Patient
from .forms import RegisterForm, PatientForm, TattooForm, ScarForm


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request=request, template_name="accounts/login.html", context={"form": form})


class HomeView(TemplateView):
    template_name = 'accounts/home.html'

class ContactView(TemplateView):
    template_name = 'accounts/contact.html'

class AboutView(TemplateView):
    template_name = 'accounts/about.html'

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

class UserCadastroPac(TemplateView):
    template_name = 'accounts/cadastro_pac.html'

class UserRegisterView(TemplateView):
    patient_form_class = PatientForm
    register_form_class = RegisterForm
    tattoo_form_class = TattooForm
    scar_form_class = ScarForm
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
        context['tattoo_form'] = self.tattoo_form_class
        context['scar_form'] = self.scar_form_class
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
        self.tattoo_form = self.tattoo_form_class(
            post_data,
            **kwargs
        )
        self.scar_form = self.scar_form_class(
            post_data,
            **kwargs
        )

    def post(self, request, *args, **kwargs):
        self.init_forms(request.POST)
        if self.validate_forms():
            self.save_forms(request)
        return redirect(self.success_url)

    def validate_forms(self):
        return all([
            self.register_form.is_valid(),
            self.patient_form.is_valid(),
            self.tattoo_form.is_valid(),
            self.scar_form.is_valid()
        ])

    def save_forms(self, request):
        self.register_form.save()
        self.patient_form.save(request)
        self.tattoo_form.save()
        self.scar_form.save()

