# Generated by Django 3.0.8 on 2022-06-01 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20220601_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='Reason',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
