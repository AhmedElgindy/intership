# Generated by Django 4.2 on 2023-06-15 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_userprofile_is_doctor_userprofile_is_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]