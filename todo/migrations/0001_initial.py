# Generated by Django 3.2.4 on 2021-06-19 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('commpleted', models.BooleanField(default=False)),
                ('timeCreated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]