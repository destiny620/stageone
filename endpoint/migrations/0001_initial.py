# Generated by Django 4.2.5 on 2023-09-11 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack_name', models.CharField(max_length=50)),
                ('current_day', models.CharField(max_length=50)),
                ('utc_time', models.DateTimeField(verbose_name='2023-09-11T15:52:27Z')),
                ('track', models.CharField(max_length=50)),
                ('github_file_url', models.CharField(max_length=50)),
                ('github_repo_url', models.CharField(max_length=50)),
                ('status_code', models.IntegerField(default=200)),
            ],
        ),
    ]