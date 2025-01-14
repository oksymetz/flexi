# Generated by Django 5.1.4 on 2025-01-13 15:21

import product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_material_thickness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='box_depth',
            field=models.FloatField(validators=[product.models.validate_range]),
        ),
        migrations.AlterField(
            model_name='box',
            name='box_height',
            field=models.FloatField(validators=[product.models.validate_range]),
        ),
        migrations.AlterField(
            model_name='box',
            name='box_length',
            field=models.FloatField(validators=[product.models.validate_range]),
        ),
    ]
