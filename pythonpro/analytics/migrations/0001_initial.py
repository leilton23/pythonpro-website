# Generated by Django 2.2.6 on 2019-11-21 01:20

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'sessão',
                'verbose_name_plural': 'sessões',
            },
        ),
        migrations.CreateModel(
            name='PageView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('meta', django.contrib.postgres.fields.jsonb.JSONField()),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='analytics.UserSession', verbose_name='sessão')),
            ],
            options={
                'verbose_name': 'page view',
                'verbose_name_plural': 'page views',
            },
        ),
    ]
