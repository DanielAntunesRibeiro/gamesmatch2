# Generated by Django 4.1.2 on 2022-10-14 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchapp', '0002_alter_perfil_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cpf',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
