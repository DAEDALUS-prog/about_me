# Generated by Django 4.0.6 on 2022-07-05 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Эл. почта')),
                ('content_message', models.TextField(max_length=200, verbose_name='Письмо')),
                ('date_message', models.DateTimeField(auto_now_add=True, verbose_name='Время получения')),
            ],
            options={
                'ordering': ['-date_message'],
            },
        ),
    ]