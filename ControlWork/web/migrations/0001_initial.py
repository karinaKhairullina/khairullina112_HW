# Generated by Django 4.1.2 on 2022-10-29 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbid', models.CharField(max_length=10, verbose_name='ID пользователя')),
                ('to_do', models.CharField(max_length=30, verbose_name='Что сделать?')),
                ('done', models.CharField(max_length=30, verbose_name='Что сделано?')),
                ('created_at', models.CharField(max_length=30)),
                ('until_date', models.DateField(verbose_name='Дата создания')),
            ],
        ),
    ]
