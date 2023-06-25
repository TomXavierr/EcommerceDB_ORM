# Generated by Django 4.2.2 on 2023-06-24 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_color_color_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='color_code',
        ),
        migrations.RemoveField(
            model_name='products',
            name='product_sport',
        ),
        migrations.AddField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='brand_logos/'),
        ),
        migrations.AddField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='category_thumbnails/'),
        ),
        migrations.DeleteModel(
            name='Sport',
        ),
    ]