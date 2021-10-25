from django.db import models

# Create your models here.
from django.forms import model_to_dict


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre')

    def toJSON(self):
        item = model_to_dict(self)
        return item
