from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Patient, Scar, Tattoo

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            return password1
        return None

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        fields = ['date_of_birth', 'sex', 'eye_color', 'gender', 'blood_type', 'cpf', 'rg', 'continuous_medication', 'medication', 'state', 'hair_color', 'birthmark']