# Generated by Django 2.1.5 on 2019-01-30 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_auto_20190129_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='book',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='application.Book'),
        ),
    ]