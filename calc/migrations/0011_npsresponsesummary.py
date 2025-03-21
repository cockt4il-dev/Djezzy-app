# Generated by Django 5.1.6 on 2025-03-21 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0010_npsoverview'),
    ]

    operations = [
        migrations.CreateModel(
            name='NPSResponseSummary',
            fields=[
                ('response_parsed', models.IntegerField(primary_key=True, serialize=False)),
                ('response_count', models.BigIntegerField()),
            ],
            options={
                'db_table': 'nps_responses_distribution',
                'ordering': ['response_parsed'],
                'managed': False,
            },
        ),
    ]
