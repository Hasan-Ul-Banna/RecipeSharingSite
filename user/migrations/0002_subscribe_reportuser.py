# Generated by Django 4.1 on 2022-08-14 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribed_by', to=settings.AUTH_USER_MODEL)),
                ('subscribed_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribed_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReportUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_by', to=settings.AUTH_USER_MODEL)),
                ('reported_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]