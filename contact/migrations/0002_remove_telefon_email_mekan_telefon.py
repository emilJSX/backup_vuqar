# Generated by Django 3.2.11 on 2022-03-14 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telefon_email_mekan',
            name='telefon',
        ),
    ]