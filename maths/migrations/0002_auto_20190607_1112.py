# Generated by Django 2.1 on 2019-06-07 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maths',
            name='description',
            field=models.TextField(default='No description', max_length=2500),
        ),
    ]
