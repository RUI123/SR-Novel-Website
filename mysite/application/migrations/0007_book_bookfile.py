# Generated by Django 2.0.2 on 2019-01-28 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_auto_20190121_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookFile',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
