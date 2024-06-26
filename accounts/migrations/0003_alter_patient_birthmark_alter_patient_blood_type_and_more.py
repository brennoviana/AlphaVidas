# Generated by Django 5.0.6 on 2024-06-25 19:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_patient_telephone_scar_has_scar_tattoo_has_tattoo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='birthmark',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_type',
            field=models.CharField(blank=True, choices=[('', '---'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='continuous_medication',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ethnicity',
            field=models.CharField(blank=True, choices=[('', '---'), ('Branco', 'Branco'), ('Negro', 'Negro'), ('Asiático', 'Asiático'), ('Indígena', 'Indígena'), ('Pardo', 'Pardo'), ('Outro', 'Outro')], default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='eye_color',
            field=models.CharField(blank=True, choices=[('', '---'), ('Castanho', 'Castanho'), ('Azul', 'Azul'), ('Verde', 'Verde'), ('Cinza', 'Cinza'), ('Outra', 'Outra')], default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('', '---'), ('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Não-binário', 'Não-binário'), ('Gênero fluído', 'Gênero fluído'), ('Transgênero masculino', 'Transgênero masculino'), ('Transgênero feminino', 'Transgênero feminino'), ('Outro', 'Outro')], default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='hair_color',
            field=models.CharField(blank=True, choices=[('', '---'), ('Preto', 'Preto'), ('Castanho escuro', 'Castanho escuro'), ('Castanho médio', 'Castanho médio'), ('Castanho claro', 'Castanho claro'), ('Loiro escuro', 'Loiro escuro'), ('Loiro médio', 'Loiro médio'), ('Loiro claro', 'Loiro claro'), ('Ruivo', 'Ruivo'), ('Outra', 'Outra')], default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='height',
            field=models.FloatField(blank=True, default=140, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='rg',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(blank=True, choices=[('', '---'), ('Masculino', 'Masculino'), ('Feminino', 'Feminino')], default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='state',
            field=models.CharField(blank=True, choices=[('', '---------------'), ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='scar',
            name='has_scar',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='scar',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.patient'),
        ),
        migrations.AlterField(
            model_name='scar',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tattoo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tattoo',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.patient'),
        ),
        migrations.AlterField(
            model_name='tattoo',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
