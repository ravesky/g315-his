# Generated by Django 2.2.3 on 2019-08-07 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('birth_date', models.DateField()),
                ('father_name', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=80)),
                ('district', models.CharField(max_length=40)),
                ('mobile', models.IntegerField()),
                ('ID_number', models.IntegerField()),
                ('ID_type', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('pincode', models.CharField(max_length=6)),
                ('village', models.CharField(max_length=40)),
            ],
        ),
    ]
