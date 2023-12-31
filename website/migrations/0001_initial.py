# Generated by Django 4.2 on 2023-09-14 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=25)),
                ('owner_image', models.ImageField(upload_to='', verbose_name='owner/')),
                ('owner_about', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(upload_to='logo/')),
                ('favicon', models.ImageField(upload_to='favicon/')),
                ('home_title', models.CharField(max_length=150)),
                ('scroll_button', models.CharField(max_length=20)),
                ('facebook', models.CharField(max_length=50)),
                ('twitter', models.CharField(max_length=50)),
                ('instagram', models.CharField(max_length=50)),
                ('dribble', models.CharField(max_length=50)),
                ('about_pre_title', models.CharField(max_length=15)),
                ('about_title', models.CharField(max_length=30)),
                ('about_background_image', models.ImageField(upload_to='', verbose_name='about/')),
                ('about_desc', models.TextField(blank=True, null=True)),
                ('expertise_pre_title', models.CharField(max_length=15)),
                ('expertise_title', models.CharField(max_length=30)),
                ('expertise_desc', models.TextField(max_length=300)),
                ('expertise_button_text', models.CharField(max_length=20)),
                ('clients_pre_title', models.CharField(max_length=15)),
                ('clients_title', models.CharField(max_length=30)),
                ('clients_desc', models.TextField(blank=True, null=True)),
                ('testimonials_pre_title', models.CharField(max_length=20)),
                ('testimonials_title', models.CharField(max_length=30)),
                ('cta_title', models.CharField(max_length=30)),
                ('cta_desc', models.TextField(max_length=200)),
                ('cta_button', models.CharField(max_length=20)),
                ('article_pre_title', models.CharField(max_length=15)),
                ('article_title', models.CharField(max_length=30)),
                ('newsLetter_title', models.CharField(max_length=20)),
                ('newsLetter_desc', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=30)),
                ('alt_email', models.EmailField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('alt_phone', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
