# Generated by Django 5.1.3 on 2024-12-12 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baptism', '0005_baptismadvanced_logindetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baptismadvanced',
            name='question_type',
            field=models.CharField(choices=[('MULTIPLE', 'MULTIPLE'), ('MULTIPLE-SELECT', 'MULTIPLE-SELECT'), ('TEXT-AREA', 'TEXT-AREA')], default='MULTIPLE', max_length=255),
        ),
    ]