# Generated by Django 3.1.6 on 2021-04-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_userdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_img',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]
