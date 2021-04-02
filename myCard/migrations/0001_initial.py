# Generated by Django 2.2.17 on 2021-04-01 19:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(

            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=150)),
                ('phone_no', models.BigIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('location', models.CharField(blank=True, max_length=150)),
                ('occupation', models.CharField(blank=True, max_length=50)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('media_links', models.URLField(blank=True)),
                ('about', models.CharField(blank=True, max_length=150)),
                ('visibility', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
