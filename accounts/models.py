from django.contrib.auth.models import User
from django.db import models

GENDER_CHOICES = [
    ('', '---'),
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
    ('Não-binário', 'Não-binário'),
    ('Gênero fluído', 'Gênero fluído'),
    ('Transgênero masculino', 'Transgênero masculino'),
    ('Transgênero feminino', 'Transgênero feminino'),
    ('Outro', 'Outro'),
]

SEX_CHOICES = [
    ('', '---'),
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
]

EYE_COLOR_CHOICES = [
    ('', '---'),
    ('Castanho', 'Castanho'),
    ('Azul', 'Azul'),
    ('Verde', 'Verde'),
    ('Cinza', 'Cinza'),
    ('Outra', 'Outra'),
]

ETHNICITY_CHOICES = [
    ('', '---'),
    ('Branco', 'Branco'),
    ('Negro', 'Negro'),
    ('Asiático', 'Asiático'),
    ('Indígena', 'Indígena'),
    ('Pardo', 'Pardo'),
    ('Outro', 'Outro'),
]

HAIR_COLOR_CHOICES = [
    ('', '---'),
    ('Preto', 'Preto'),
    ('Castanho escuro', 'Castanho escuro'),
    ('Castanho médio', 'Castanho médio'),
    ('Castanho claro', 'Castanho claro'),
    ('Loiro escuro', 'Loiro escuro'),
    ('Loiro médio', 'Loiro médio'),
    ('Loiro claro', 'Loiro claro'),
    ('Ruivo', 'Ruivo'),
    ('Outra', 'Outra'),
]

BLOOD_TYPE_CHOICES = [
    ('', '---'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

BRAZIL_CHOICES = [
        ('', '---------------'),
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
]

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    rg = models.CharField(max_length=9, blank=True, null=True)
    telephone = models.CharField(max_length=11, blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, default='', blank=True, null=True)
    sex = models.CharField(max_length=255, choices=SEX_CHOICES, default='', blank=True, null=True)
    eye_color = models.CharField(max_length=255, choices=EYE_COLOR_CHOICES, default='', blank=True, null=True)
    ethnicity = models.CharField(max_length=255, choices=ETHNICITY_CHOICES, default='', blank=True, null=True)
    height = models.FloatField(blank=True, null=True, default=140)
    hair_color = models.CharField(max_length=255, choices=HAIR_COLOR_CHOICES, default='', blank=True, null=True)
    blood_type = models.CharField(max_length=255, choices=BLOOD_TYPE_CHOICES, default='', blank=True, null=True)
    continuous_medication = models.BooleanField(default=False, blank=True, null=True)
    medication = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=2, choices=BRAZIL_CHOICES, default='', blank=True, null=True)
    birthmark = models.BooleanField(default=False, blank=True, null=True)

class Tattoo(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    has_tattoo = models.BooleanField(default=False)
    type = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class Scar(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    has_scar = models.BooleanField(default=False, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
