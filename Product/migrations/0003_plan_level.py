# Generated by Django 2.1.11 on 2020-01-06 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]