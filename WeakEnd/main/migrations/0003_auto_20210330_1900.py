# Generated by Django 3.1 on 2021-03-30 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_profile_user_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sub_first',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sub_second',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sub_third',
            field=models.DateTimeField(null=True),
        ),
    ]
