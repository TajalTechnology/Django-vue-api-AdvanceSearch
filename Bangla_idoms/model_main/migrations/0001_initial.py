# Generated by Django 3.0.4 on 2020-03-13 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bn_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bn_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bn_name', models.CharField(max_length=100)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model_main.Division')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChandaKatha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bn_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=300)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model_main.Category')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model_main.District')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
