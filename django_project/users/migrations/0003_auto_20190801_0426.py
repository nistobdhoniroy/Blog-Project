# Generated by Django 2.2.3 on 2019-07-31 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190731_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='profile_pics'),
        ),
    ]
