# Generated by Django 3.2 on 2021-12-01 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='missioncontent',
            name='ourbelief',
        ),
        migrations.DeleteModel(
            name='OurMission',
        ),
        migrations.DeleteModel(
            name='MissionContent',
        ),
    ]