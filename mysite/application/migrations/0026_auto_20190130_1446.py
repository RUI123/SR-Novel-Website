# Generated by Django 2.1.5 on 2019-01-30 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0025_auto_20190130_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookImage',
            field=models.FileField(default='default_book.jpg', upload_to='book_images'),
        ),
    ]
