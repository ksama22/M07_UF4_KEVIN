# Generated by Django 4.1.7 on 2023-04-13 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
            ],
        ),
    ]
