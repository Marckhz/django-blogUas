# Generated by Django 3.0 on 2020-01-24 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200122_0409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organigrama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organigrama', models.ImageField(upload_to='')),
            ],
        ),
    ]