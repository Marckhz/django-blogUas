# Generated by Django 3.0 on 2020-01-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_organigrama'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendars',
            name='calendar',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curricularplan',
            name='curricular_plan',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
