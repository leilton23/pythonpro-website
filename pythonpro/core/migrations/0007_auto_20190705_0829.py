# Generated by Django 2.2.2 on 2019-07-05 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_user_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='source',
            field=models.CharField(default='unknown', max_length=255, verbose_name='source'),
        ),
    ]
