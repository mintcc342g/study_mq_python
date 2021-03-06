# Generated by Django 3.1.3 on 2020-12-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('user_id', models.BigIntegerField()),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'events',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('user_id', models.BigIntegerField()),
                ('message', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'messages',
                'managed': True,
            },
        ),
    ]
