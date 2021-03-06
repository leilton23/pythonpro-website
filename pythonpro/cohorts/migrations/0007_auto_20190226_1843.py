# Generated by Django 2.1.7 on 2019-02-26 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohorts', '0006_auto_20190226_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webinar',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='webinar',
            name='discourse_topic_id',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='webinar',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='webinars/'),
        ),
    ]
