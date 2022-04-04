# Generated by Django 3.1.3 on 2022-04-04 13:17

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='nome', unique=True),
        ),
    ]