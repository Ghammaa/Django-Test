# Generated by Django 3.0 on 2022-01-24 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20220119_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profpic',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/'),
        ),
    ]