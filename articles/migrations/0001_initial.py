# Generated by Django 3.2.13 on 2022-11-11 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='img/default_image.jpeg', upload_to='img/')),
                ('name', models.CharField(blank=True, max_length=80)),
                ('brand', models.CharField(blank=True, max_length=50)),
                ('connect', models.CharField(blank=True, max_length=50)),
                ('array', models.CharField(blank=True, max_length=50)),
                ('switch', models.CharField(blank=True, max_length=50)),
                ('key_switch', models.CharField(blank=True, max_length=50)),
                ('press', models.CharField(blank=True, max_length=50)),
                ('weight', models.CharField(blank=True, max_length=50)),
                ('kind', models.CharField(blank=True, max_length=50)),
                ('article_like', models.ManyToManyField(related_name='like_article', to=settings.AUTH_USER_MODEL)),
                ('mark', models.ManyToManyField(related_name='marker', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
