# Generated by Django 2.1.5 on 2019-02-03 03:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0028_auto_20190202_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]