# Generated by Django 4.2.2 on 2023-06-27 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_remove_colorvariation_variation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variants',
            old_name='stock',
            new_name='sku',
        ),
        migrations.RemoveField(
            model_name='products',
            name='product_gender',
        ),
        migrations.AddField(
            model_name='variants',
            name='product_description',
            field=models.TextField(default=False, max_length=300),
        ),
    ]