# Generated by Django 4.2.3 on 2024-01-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produzione', '0014_order_order_customization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_customization',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
    ]
