# Generated by Django 5.1.2 on 2025-05-05 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0013_alter_property_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exclusive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='exclusive/')),
                ('name', models.TextField()),
                ('starts_at', models.PositiveIntegerField(default=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Trending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='trending')),
                ('name', models.TextField()),
            ],
        ),
    ]
