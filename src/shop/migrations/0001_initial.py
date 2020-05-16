# Generated by Django 2.1 on 2018-08-18 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='著者名')),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('price', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='価格')),
                ('description', models.TextField(blank=True, null=True, verbose_name='概要')),
                ('publish_date', models.DateField(blank=True, null=True, verbose_name='出版日')),
                ('authors', models.ManyToManyField(to='shop.Author', verbose_name='著者')),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='出版社名')),
            ],
            options={
                'db_table': 'publisher',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.Publisher', verbose_name='出版社'),
        ),
    ]