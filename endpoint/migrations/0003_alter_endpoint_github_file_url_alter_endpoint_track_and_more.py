# Generated by Django 4.1.7 on 2023-09-11 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoint', '0002_alter_endpoint_utc_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='github_file_url',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='track',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='utc_time',
            field=models.DateTimeField(verbose_name='2023-09-11T20:56:46Z'),
        ),
    ]
