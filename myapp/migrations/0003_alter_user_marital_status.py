# Generated by Django 4.0.1 on 2022-01-26 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_marital_status_alter_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='marital_status',
            field=models.CharField(default='unmarried', max_length=8, null=True),
        ),
    ]
