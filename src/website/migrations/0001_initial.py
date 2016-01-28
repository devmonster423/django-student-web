# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-28 16:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_markdown.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', django_markdown.models.MarkdownField()),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('prof_pic', models.ImageField(blank=True, null=True, upload_to='author_profile_pics/%Y-%m-%d/')),
                ('blurb', django_markdown.models.MarkdownField()),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('convenor', models.CharField(max_length=100)),
                ('strength', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=300)),
                ('details', models.CharField(max_length=2000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('ctype', models.CharField(choices=[('H', 'HCC'), ('S', 'Security'), ('L', 'LAN'), ('P', 'Sports'), ('E', 'Eateries'), ('I', 'Independent Bodies'), ('A', 'Academics'), ('M', 'Miscellaneous')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=2000)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('contact', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('CH', 'Chemical Engineering'), ('CO', 'Computer Engineering'), ('CV', 'Civil Engineering'), ('EC', 'Electronics and Communications Engineering'), ('EE', 'Elelctrical and Electronics Engineering'), ('IT', 'Information Technology'), ('ME', 'Mechanical Engineering'), ('MN', 'Mining Engineering'), ('MT', 'Materials and Metallurgical Engineering')], max_length=2)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=1000)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('details', models.CharField(max_length=2000)),
                ('category', models.CharField(choices=[('C', 'Campus News'), ('N', 'In the News'), ('S', 'Spotlight')], max_length=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('pinned', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Author'),
        ),
    ]
