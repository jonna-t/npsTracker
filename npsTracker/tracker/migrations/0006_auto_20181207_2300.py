# Generated by Django 2.1.3 on 2018-12-07 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20181207_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='assigned_team',
            field=models.CharField(choices=[('NISPI/DWP', 'NISPI/DWP')], max_length=20),
        ),
    ]