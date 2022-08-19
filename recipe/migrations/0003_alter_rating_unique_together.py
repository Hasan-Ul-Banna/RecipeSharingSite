# Generated by Django 4.1 on 2022-08-17 08:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0002_reportrecipe'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('rating_owner', 'recipe')},
        ),
    ]
