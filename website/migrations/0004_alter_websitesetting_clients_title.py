# Generated by Django 4.2 on 2023-09-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_websitesetting_cta_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitesetting',
            name='clients_title',
            field=models.CharField(max_length=60),
        ),
    ]