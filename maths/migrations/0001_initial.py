# Generated by Django 2.1 on 2019-06-07 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Maths',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('sub_topic', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='images/')),
                ('description', models.TextField(default='No description', max_length=300)),
                ('grade', models.IntegerField(default='0')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
