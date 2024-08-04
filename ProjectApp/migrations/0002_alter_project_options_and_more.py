# Generated by Django 5.0.7 on 2024-08-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'پروژه', 'verbose_name_plural': 'پروژه ها'},
        ),
        migrations.RenameField(
            model_name='benefit',
            old_name='text',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default=1, max_length=255, verbose_name='اسلاگ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='category_slug',
            field=models.CharField(default=1, max_length=255, verbose_name='دسته بندی'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.ManyToManyField(related_name='project', to='ProjectApp.category'),
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.CharField(max_length=255, verbose_name='تاریخ اجرای پروژه'),
        ),
    ]
