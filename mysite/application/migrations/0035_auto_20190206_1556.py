# Generated by Django 2.1.5 on 2019-02-06 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0034_auto_20190206_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookImage',
            field=models.ImageField(default='default_book.jpg', upload_to='book_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.FileField(default='default_profile.jpg', upload_to='profile_images'),
        ),
    ]
