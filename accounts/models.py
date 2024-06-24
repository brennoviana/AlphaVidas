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

MEDICATION_CHOICES = [
    ('', '---'),
    ('Sim', 'Sim'),
    ('Nao', 'Não'),
]

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=9)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    eye_color = models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)
    height = models.FloatField()
    hair_color = models.CharField(max_length=255)
    blood_type = models.CharField(max_length=255)
    continuous_medication = models.CharField(max_length=255)
    medication = models.CharField(max_length=255)

class Tattoo(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    description = models.TextField()

class Scar(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)

