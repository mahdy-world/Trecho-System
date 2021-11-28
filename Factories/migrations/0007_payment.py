# Generated by Django 3.2.5 on 2021-11-28 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Factories', '0006_alter_factory_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الاضافة')),
                ('price', models.IntegerField(verbose_name='المبلغ')),
                ('recipient', models.CharField(max_length=50, verbose_name='المستلم')),
                ('admin', models.CharField(max_length=50, verbose_name='المسئول')),
                ('date', models.DateField(verbose_name='التاريخ')),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Factories.factory', verbose_name='المصنع')),
            ],
        ),
    ]
