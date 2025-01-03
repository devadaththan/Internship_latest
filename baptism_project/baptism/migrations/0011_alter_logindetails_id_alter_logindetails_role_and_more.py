# Generated by Django 5.1.4 on 2024-12-14 10:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("baptism", "0010_rename_user_id_logindetails_id_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="logindetails",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="logindetails",
            name="role",
            field=models.CharField(
                choices=[
                    ("Priest", "Priest"),
                    ("Admin", "Admin"),
                    ("Public", "Public"),
                    ("Secretary", "Secretary"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="logindetails",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="logindetails",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
