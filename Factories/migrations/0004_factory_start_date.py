# Generated by Django 3.2.5 on 2021-11-28 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Factories', '0003_factory_machine_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='factory',
            name='start_date',
            field=models.DateField(null=True, verbose_name='تاريخ البداية'),
        ),
    ]