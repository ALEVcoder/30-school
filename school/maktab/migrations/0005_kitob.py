# Generated by Django 3.1.3 on 2021-01-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maktab', '0004_photolar'),
    ]

    operations = [
        migrations.CreateModel(
            name='kitob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitob_nomi', models.CharField(max_length=50)),
                ('malumot', models.TextField()),
                ('kiritish', models.FileField(upload_to='kitoblar')),
            ],
        ),
    ]
