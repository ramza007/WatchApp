# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-27 18:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appwatch', '0003_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='business/')),
                ('business_name', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('estate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appwatch.Neighborhood')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
