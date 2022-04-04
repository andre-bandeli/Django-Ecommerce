# Generated by Django 3.1.3 on 2022-04-04 13:18

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20220404_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='nome', unique=True),
        ),
    ]
