# Generated by Django 3.1 on 2021-05-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210511_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='vulnlist',
            name='cookie',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='vulnlist',
            name='level',
            field=models.IntegerField(blank=True, default=2),
        ),
    ]