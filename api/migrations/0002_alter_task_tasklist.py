# Generated by Django 3.2.3 on 2021-05-20 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tasklist',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.tasklist'),
        ),
    ]
