# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __unicode__(self):
        return self.nombre


class Editorial(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Título')
    editorial = models.ForeignKey(Editorial)
    autor = models.ManyToManyField(Autor)
