# Generated by Django 3.1.3 on 2022-05-24 14:44

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_producthome'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductHomeList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('image', models.ImageField(blank=True, upload_to='produto//%Y/%m/%d')),
                ('descricao', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produto', to='produto.category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.DeleteModel(
            name='ProductHome',
        ),
    ]