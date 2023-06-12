# Generated by Django 4.2.2 on 2023-06-10 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='variants',
            name='stock',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='variants',
            name='variant_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
