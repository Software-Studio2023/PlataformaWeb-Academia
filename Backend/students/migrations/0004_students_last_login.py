# Generated by Django 4.1 on 2023-11-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_students_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]