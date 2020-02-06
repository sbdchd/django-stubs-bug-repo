# Generated by Django 2.2 on 2020-02-06 01:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('github_id', models.IntegerField()),
                ('github_login', models.CharField(max_length=255)),
                ('github_access_token', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]