# Generated by Django 2.2.12 on 2020-05-16 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=255, verbose_name='テスト名')),
                ('test_description', models.CharField(max_length=255, verbose_name='テスト名')),
                ('test_count', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='テスト名')),
            ],
            options={
                'db_table': 'projects',
            },
        ),
    ]
