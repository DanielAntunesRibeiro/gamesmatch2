# Generated by Django 4.1.2 on 2022-10-14 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='perfil',
            fields=[
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('game1', models.CharField(max_length=255)),
                ('pontuacao1', models.PositiveIntegerField()),
                ('game2', models.CharField(blank=True, max_length=255, null=True)),
                ('pontuacao2', models.PositiveIntegerField(blank=True, null=True)),
                ('dat_nasc', models.DateField()),
                ('nickname', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('cep', models.PositiveIntegerField(blank=True, null=True)),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('zone', models.CharField(max_length=100)),
            ],
        ),
    ]
