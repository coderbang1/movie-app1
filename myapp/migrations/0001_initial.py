# Generated by Django 3.1 on 2020-09-25 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('release', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('price', models.FloatField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.genere')),
            ],
        ),
    ]
