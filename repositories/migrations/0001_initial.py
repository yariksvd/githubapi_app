# Generated by Django 2.2.7 on 2019-11-27 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReposModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('html_url', models.CharField(max_length=1024)),
                ('description', models.TextField(null=True)),
                ('private', models.BooleanField()),
                ('created_at', models.CharField(max_length=255)),
                ('watchers', models.PositiveIntegerField()),
            ],
        ),
    ]
