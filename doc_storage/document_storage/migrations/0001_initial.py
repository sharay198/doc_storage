# Generated by Django 4.2 on 2023-05-03 16:19

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalDocument',
            fields=[
                ('id',
                 models.BigIntegerField(auto_created=True,
                                        blank=True,
                                        db_index=True,
                                        verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('history_id',
                 models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason',
                 models.CharField(max_length=100, null=True)),
                ('history_type',
                 models.CharField(choices=[('+', 'Created'), ('~', 'Changed'),
                                           ('-', 'Deleted')],
                                  max_length=1)),
                ('history_user',
                 models.ForeignKey(
                     null=True,
                     on_delete=django.db.models.deletion.SET_NULL,
                     related_name='+',
                     to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical document',
                'verbose_name_plural': 'historical documents',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
