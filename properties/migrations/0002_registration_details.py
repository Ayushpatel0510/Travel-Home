# Generated by Django 5.1.2 on 2024-12-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('pincode', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
