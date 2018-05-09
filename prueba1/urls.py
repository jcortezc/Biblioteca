"""prueba1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.lista_libros, name='lista_libro'),
    url(r'^nuevo/$', views.ingresa_libro, name='ingresa_libro'),
    url(r'^edita/(?P<pk>\d+)/$', views.edita_libro, name='edita_libro'),
    url(r'^borrar/(?P<pk>\d+)/$', views.borrar_libro, name='borrar_libro'),
]
