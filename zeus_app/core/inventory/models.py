from django.db import models

from django.forms import model_to_dict


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item


class Trademarks(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item


class Products(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    category = models.ForeignKey(Categories, on_delete=models.RESTRICT, verbose_name='Categoria')
    trademark = models.ForeignKey(Trademarks, on_delete=models.RESTRICT, verbose_name='Marca')
    detail = models.CharField(max_length=500, verbose_name='Detalle')
    price_buy = models.DecimalField(default=0.00, max_digits=12, decimal_places=2, verbose_name='Precio Compra')
    price_sell_min = models.DecimalField(default=0.00, max_digits=12, decimal_places=2, verbose_name='Precio Venta Minorista')
    price_sell_may = models.DecimalField(default=0.00, max_digits=12, decimal_places=2, verbose_name='Precio Venta Mayorista')
    stock = models.IntegerField(default=0, verbose_name='Stock')

    def toJSON(self):
        item = model_to_dict(self)
        return item
