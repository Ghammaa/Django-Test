# Generated by Django 3.0 on 2022-01-17 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]