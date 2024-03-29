# Generated by Django 4.2.8 on 2024-01-10 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CarDealer', '0001_initial'),
        ('Car', '0002_initial'),
        ('Client', '0001_initial'),
        ('Supplier', '0001_initial'),
        ('History', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suppliersaleshistory',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supplier.supplier'),
        ),
        migrations.AddField(
            model_name='salesdealerhistory',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.car', verbose_name='Car'),
        ),
        migrations.AddField(
            model_name='salesdealerhistory',
            name='car_dealer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDealer.cardealer', verbose_name='Car Dealer'),
        ),
        migrations.AddField(
            model_name='salesdealerhistory',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.client'),
        ),
    ]
