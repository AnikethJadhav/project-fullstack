# Generated by Django 4.0.1 on 2022-01-24 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
            ],
        ),
    ]
