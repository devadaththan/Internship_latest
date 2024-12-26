# Generated by Django 5.1.3 on 2024-12-12 13:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baptism', '0006_alter_baptismadvanced_question_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldTable',
            fields=[
                ('field_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_no', models.IntegerField()),
                ('type', models.CharField(choices=[('READING', 'READING'), ('SONG', 'SONG'), ('PRAYER', 'PRAYER'), ('REMARKS', 'REMARKS'), ('AUTHORIZATION', 'AUTHORIZATION'), ('FINANCIAL', 'FINANCIAL'), ('SPECIAL SAINTS', 'SPECIAL SAINTS')], default='READING', max_length=255)),
                ('data', models.TextField()),
                ('choice', models.CharField(choices=[('MULTIPLE', 'MULTIPLE'), ('MULTIPLE-SELECT', 'MULTIPLE-SELECT'), ('TEXT-AREA', 'TEXT-AREA')], default='MULTIPLE', max_length=255)),
                ('q_id', models.IntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=10)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]