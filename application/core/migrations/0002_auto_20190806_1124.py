# Generated by Django 2.2.3 on 2019-08-06 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age_firstentry',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(max_length=80),
        ),
    ]
