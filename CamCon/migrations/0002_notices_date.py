# Generated by Django 2.1.5 on 2019-08-13 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CamCon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notices',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
