# Generated by Django 3.2.9 on 2021-12-05 17:34

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
                ('name', models.CharField(max_length=70)),
                ('roll', models.IntegerField(unique=True)),
                ('city', models.CharField(max_length=200)),
                ('marks', models.IntegerField()),
                ('pass_date_time', models.DateTimeField(null=True)),
                ('pass_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]