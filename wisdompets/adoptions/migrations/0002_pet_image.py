# Generated by Django 5.0.3 on 2024-03-31 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
