# Generated by Django 3.2.6 on 2021-09-04 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_community_videolink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='videolink',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
