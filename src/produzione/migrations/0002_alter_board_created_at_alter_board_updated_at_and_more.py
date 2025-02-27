# Generated by Django 4.2.3 on 2023-07-20 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produzione', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='smt',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='smt',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='verify',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='verify',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
