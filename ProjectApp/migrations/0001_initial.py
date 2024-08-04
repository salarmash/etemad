# Generated by Django 5.0.7 on 2024-08-04 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('subtitle', models.CharField(max_length=100, verbose_name='زیرنویس')),
                ('text', models.TextField(verbose_name='متن')),
            ],
            options={
                'verbose_name': 'فایده',
                'verbose_name_plural': 'فایده ها',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, verbose_name='نام دسته بندی')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='BenefitItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='Icon', verbose_name='آیکون')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('text', models.TextField(verbose_name='متن')),
                ('benefit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='ProjectApp.benefit')),
            ],
            options={
                'verbose_name': 'آیتم',
                'verbose_name_plural': 'آیتم ها',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان پروژه')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Projects', verbose_name='تصویر')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')),
                ('category', models.ManyToManyField(related_name='projects', to='ProjectApp.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'پروژه',
                'verbose_name_plural': 'پروژه ها',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=100, verbose_name='زیرنویس')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان روی عکس')),
                ('bgImage', models.ImageField(blank=True, null=True, upload_to='Projects', verbose_name='تصویر پس زمینه')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='intro', to='ProjectApp.project')),
            ],
            options={
                'verbose_name': 'معرفی کل پروژه',
                'verbose_name_plural': 'معرفی کلی پروژه',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Projects', verbose_name='عکس')),
                ('alt', models.CharField(max_length=200)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ProjectApp.project')),
            ],
            options={
                'verbose_name': 'نگاره',
                'verbose_name_plural': 'گالری',
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255, verbose_name='لیبیل')),
                ('value', models.CharField(max_length=255, verbose_name='مقدار')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='ProjectApp.project')),
            ],
            options={
                'verbose_name': 'جزئیات',
                'verbose_name_plural': 'جزئیات',
            },
        ),
        migrations.CreateModel(
            name='Descriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان توضیحات')),
                ('subtitle', models.CharField(max_length=100, verbose_name='زیر نویس عنوان')),
                ('content', models.TextField(verbose_name='متن توضیحات پروژه')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='description', to='ProjectApp.project')),
            ],
            options={
                'verbose_name': 'توضیح',
                'verbose_name_plural': 'توضیجات',
            },
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Projects', verbose_name='آواتار')),
                ('name', models.CharField(max_length=255, verbose_name='نام و نام خانوادگی')),
                ('role', models.CharField(max_length=155, verbose_name='موقعیت شفلی')),
                ('text', models.TextField(blank=True, null=True, verbose_name='متن')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='avatar', to='ProjectApp.project')),
            ],
            options={
                'verbose_name': 'آواتار',
                'verbose_name_plural': 'آواتارها',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان رزومه')),
                ('content', models.TextField(verbose_name='توضیح رزومه')),
                ('name', models.CharField(max_length=255, verbose_name='نام و نام خانوادگی')),
                ('role', models.CharField(max_length=155, verbose_name='موقعیت شفلی')),
                ('text', models.TextField(blank=True, null=True, verbose_name='متن')),
                ('quote', models.TextField(blank=True, null=True, verbose_name='متن')),
                ('author', models.CharField(max_length=255, verbose_name='نام نویسنده')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='ProjectApp.project')),
            ],
            options={
                'verbose_name': 'رزومه',
                'verbose_name_plural': 'رزومه ها',
            },
        ),
    ]