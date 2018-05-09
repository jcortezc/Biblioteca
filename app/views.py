# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from .forms import *


# Create your views here.
def lista_libros(request):
    if request.method == 'GET':
        if request.GET.get('buscar'):
            palabra = request.GET['buscar']
            libros = Libro.objects.filter(titulo__contains=palabra)
        else:
            libros = Libro.objects.all()
    return render(request, 'lista_libros.html', locals())


def ingresa_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista_libro'))
    form = LibroForm()
    return render(request, 'ingresa_libro.html', locals())


def edita_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista_libro'))
    form = LibroForm(instance=libro)
    return render(request, 'ingresa_libro.html', locals())


def borrar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    libro.delete()
    return redirect(reverse('lista_libro'))
