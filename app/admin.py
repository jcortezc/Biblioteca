# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


# Register your models here.
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editorial',)
    list_filter = ('autor',)
    search_fields = ('titulo',)
    filter_vertical = ('autor',)


admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Libro, LibroAdmin)
