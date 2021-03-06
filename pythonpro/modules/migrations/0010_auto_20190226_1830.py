# Generated by Django 2.1.7 on 2019-02-26 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0009_auto_20180319_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='order',
            field=models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='module',
            name='order',
            field=models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='section',
            name='order',
            field=models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='order',
            field=models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order'),
        ),
    ]
