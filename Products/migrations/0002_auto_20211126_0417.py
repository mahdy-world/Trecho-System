# Generated by Django 3.2.5 on 2021-11-26 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الاضافة'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='التكلفة'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='صورة الموديل'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='سعر البيع'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='وزن الموديل'),
        ),
    ]
