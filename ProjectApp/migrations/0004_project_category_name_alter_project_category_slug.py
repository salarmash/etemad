# Generated by Django 5.0.7 on 2024-08-04 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0003_remove_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category_name',
            field=models.CharField(default=1, max_length=255, verbose_name=' نام دسته بندی'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='category_slug',
            field=models.CharField(max_length=255, verbose_name='اسلاگ دسته بندی'),
        ),
    ]
