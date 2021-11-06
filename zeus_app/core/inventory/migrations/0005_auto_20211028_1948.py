# Generated by Django 3.2.8 on 2021-10-28 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20211027_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price_buy',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Precio Compra'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price_sell_may',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Precio Venta MAY'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price_sell_min',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Precio Venta MIN'),
        ),
    ]