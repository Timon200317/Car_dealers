# Generated by Django 4.2.7 on 2023-11-04 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Promotion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardealerpromotion',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cardealerpromotion',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='supplierpromotion',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='supplierpromotion',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
