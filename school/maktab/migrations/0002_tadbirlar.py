# Generated by Django 3.1.3 on 2021-01-15 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maktab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tadbirlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='tadbir_rasmlari')),
                ('kun', models.CharField(max_length=2)),
                ('oy', models.CharField(max_length=3)),
                ('yil', models.CharField(max_length=4)),
                ('nomi', models.CharField(max_length=25)),
                ('malumot', models.TextField(max_length=100)),
            ],
        ),
    ]
