# Generated by Django 2.1.3 on 2019-01-05 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_problem', '0008_auto_20190105_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='context_again',
            field=models.TextField(default='无', verbose_name='回头看情况'),
        ),
    ]