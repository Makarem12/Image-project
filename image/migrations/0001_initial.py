# Generated by Django 4.2.14 on 2024-07-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('tags', models.CharField(max_length=100)),
                ('pageURL', models.CharField(max_length=300)),
                ('views', models.CharField(max_length=100)),
                ('likes', models.CharField(max_length=300)),
                ('comments', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
