# Generated by Django 5.2 on 2025-04-08 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_vagas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vagas',
            old_name='nome',
            new_name='titulo',
        ),
    ]
