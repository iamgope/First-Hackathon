# Generated by Django 3.1.6 on 2021-04-06 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210403_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='Availabe',
            field=models.BooleanField(default=True),
        ),
    ]