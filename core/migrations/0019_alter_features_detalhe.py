# Generated by Django 3.2.18 on 2023-04-15 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='detalhe',
            field=models.TextField(max_length=200, verbose_name='Detalhe'),
        ),
    ]
