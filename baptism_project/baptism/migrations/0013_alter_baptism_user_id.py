# Generated by Django 5.1.4 on 2024-12-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("baptism", "0012_alter_baptism_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="baptism",
            name="user_id",
            field=models.IntegerField(default=1),
        ),
    ]