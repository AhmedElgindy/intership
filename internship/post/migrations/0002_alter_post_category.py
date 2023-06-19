# Generated by Django 4.2.2 on 2023-06-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('mental_health', 'Mental Health'), ('heart_disease', 'Heart Disease'), ('covid19', 'COVID-19'), ('immunization', 'Immunization')], max_length=100),
        ),
    ]
