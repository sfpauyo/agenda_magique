# Generated by Django 2.0.7 on 2018-07-07 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_auto_20180707_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='type',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
