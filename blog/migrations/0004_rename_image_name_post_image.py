# Generated by Django 5.1.6 on 2025-04-10 12:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_post_image_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="image_name",
            new_name="image",
        ),
    ]
