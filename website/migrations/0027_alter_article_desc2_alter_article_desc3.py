# Generated by Django 4.2 on 2024-12-10 20:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_article_desc2_article_desc3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='desc2',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='desc3',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
