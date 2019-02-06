# Generated by Django 2.1.5 on 2019-02-05 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0030_auto_20190204_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='chapterCount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select multiple genres for this book', to='application.Genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='like',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]