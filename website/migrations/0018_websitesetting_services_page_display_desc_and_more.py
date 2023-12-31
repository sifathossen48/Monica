# Generated by Django 4.2 on 2023-10-09 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_valuesitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitesetting',
            name='services_page_display_desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='websitesetting',
            name='services_page_display_title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='websitesetting',
            name='services_page_pre_title',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='websitesetting',
            name='services_page_title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
