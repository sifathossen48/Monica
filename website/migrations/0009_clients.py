# Generated by Django 4.2 on 2023-09-15 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_expertise_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=70)),
                ('image', models.ImageField(upload_to='clients/')),
            ],
        ),
    ]