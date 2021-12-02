# Generated by Django 3.2 on 2021-12-01 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_auto_20211201_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurChurch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(default='Church', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChurchContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField()),
                ('ourbelief', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.ourbelief')),
            ],
        ),
    ]
