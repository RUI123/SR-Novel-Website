# Generated by Django 2.1.5 on 2019-01-27 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('application', '0008_auto_20190126_2028'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.FileField(default='default.jpg', upload_to='profile_pics')),
                ('about_me', models.TextField(blank=True, null=True)),
                ('favorite', models.ManyToManyField(to='application.Book')),
                ('marker', models.ManyToManyField(blank=True, to='application.Marker')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
