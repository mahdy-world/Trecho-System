# Generated by Django 3.2.5 on 2021-11-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Factories', '0002_factory_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='factory',
            name='machine_count',
            field=models.IntegerField(null=True, verbose_name='عدد المكن'),
        ),
    ]