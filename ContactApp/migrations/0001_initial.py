# Generated by Django 5.0.7 on 2024-08-07 08:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('content', models.TextField(verbose_name='متن')),
            ],
            options={
                'verbose_name': 'راه ارتباطی',
                'verbose_name_plural': 'تماس با ما',
            },
        ),
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('tel', models.CharField(max_length=12, verbose_name='تلفن')),
                ('fullName', models.CharField(max_length=255, verbose_name='نام و نام خانوادگی')),
                ('message', models.TextField(verbose_name='متن در خواست')),
            ],
            options={
                'verbose_name': 'درخواست',
                'verbose_name_plural': 'درخواست ها',
            },
        ),
        migrations.CreateModel(
            name='ContactAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='ContactApp.contact')),
            ],
            options={
                'verbose_name': 'آدرس',
                'verbose_name_plural': 'آدرس ها',
            },
        ),
        migrations.CreateModel(
            name='ContactEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='ContactApp.contact')),
            ],
            options={
                'verbose_name': 'ایمیل',
                'verbose_name_plural': 'ایمیل ها',
            },
        ),
        migrations.CreateModel(
            name='ContactPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, verbose_name='تلفن')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='ContactApp.contact')),
            ],
            options={
                'verbose_name': 'تلفن',
                'verbose_name_plural': 'تلفن ها',
            },
        ),
    ]
