# Generated by Django 3.2.8 on 2021-10-27 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='price',
            new_name='price_buy',
        ),
        migrations.AddField(
            model_name='products',
            name='price_sell_may',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Precio'),
        ),
        migrations.AddField(
            model_name='products',
            name='price_sell_min',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Precio'),
        ),
    ]