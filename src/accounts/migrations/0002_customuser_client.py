# Generated by Django 2.2.12 on 2020-05-16 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200517_0843'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='projects.Client'),
            preserve_default=False,
        ),
    ]