# Generated by Django 2.2.17 on 2020-11-24 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20201124_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='places.Item'),
        ),
    ]
