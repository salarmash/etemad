# Generated by Django 5.0.7 on 2024-08-09 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceApp', '0002_alter_visionitem_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='SideBar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام کل ساید بار')),
            ],
        ),
        migrations.RemoveField(
            model_name='sidebarcounter',
            name='item',
        ),
        migrations.AlterField(
            model_name='sidebarcontent',
            name='label',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sidebarcounter',
            name='sidebar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='SideCounter', to='ServiceApp.sidebar', verbose_name='عنوان سایدبار مادر'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sidebaritem',
            name='sidebar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='SideItems', to='ServiceApp.sidebar', verbose_name='عنوان سایدبار مادر'),
            preserve_default=False,
        ),
    ]