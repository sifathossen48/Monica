# Generated by Django 4.2 on 2023-10-06 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_websitesetting_contact_page_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitesetting',
            name='email_button_text',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
