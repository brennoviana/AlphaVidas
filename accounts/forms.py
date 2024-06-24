from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Patient, Scar, Tattoo
from .models import (
    GENDER_CHOICES, EYE_COLOR_CHOICES, SEX_CHOICES,
    ETHNICITY_CHOICES, HAIR_COLOR_CHOICES, BLOOD_TYPE_CHOICES,
    MEDICATION_CHOICES
)


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
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['gender'] = forms.ChoiceField(choices=GENDER_CHOICES)
        self.fields['sex'] = forms.ChoiceField(choices=SEX_CHOICES)
        self.fields['eye_color'] = forms.ChoiceField(choices=EYE_COLOR_CHOICES)
        self.fields['ethnicity'] = forms.ChoiceField(choices=ETHNICITY_CHOICES)
        self.fields['hair_color'] = forms.ChoiceField(choices=HAIR_COLOR_CHOICES)
        self.fields['blood_type'] = forms.ChoiceField(choices=BLOOD_TYPE_CHOICES)
        self.fields['continuous_medication'] = forms.ChoiceField(choices=MEDICATION_CHOICES)

    class Meta:
        model = Patient
        fields = '__all__'
