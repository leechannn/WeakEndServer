# Generated by Django 3.1 on 2021-04-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_vulnlist_target_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='vulnlist',
            name='sub_first',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
