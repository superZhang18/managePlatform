# Generated by Django 2.1.3 on 2019-01-05 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_problem', '0006_auto_20190105_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='inspect_date',
            field=models.DateField(verbose_name='检查时间'),
        ),
    ]
