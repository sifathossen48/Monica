# Generated by Django 4.2 on 2023-10-06 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_websitesetting_contact_page_content_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitesetting',
            name='contact_page_image',
            field=models.ImageField(default=1, upload_to='contact/'),
            preserve_default=False,
        ),
    ]