# Generated by Django 4.2.3 on 2024-02-19 13:35

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_alter_announcement_announcement_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='announcement_content',
            field=django_quill.fields.QuillField(),
        ),
    ]
