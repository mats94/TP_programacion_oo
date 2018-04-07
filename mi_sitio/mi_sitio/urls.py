"""mi_sitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url

from pelicula.views import ListaGenero, CrearGenero, ModificarGenero, EliminarGenero, ListaCliente, CrearCliente, ModificarCliente, EliminarCliente

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^genero/$', ListaGenero.as_view()),
    url(r'^genero/crear/$', CrearGenero.as_view(success_url="/genero/")),
    url(r'^genero/modificar/(?P<pk>\d+)$', ModificarGenero.as_view(success_url="/genero/")),
    url(r'^genero/eliminar/(?P<pk>\d+)$', EliminarGenero.as_view(success_url="/genero/")),
    # Agregue abm clientes url
     url(r'^cliente/$', ListaCliente.as_view()),
     url(r'^cliente/crear/$', CrearCliente.as_view(success_url="/cliente/")),
     url(r'^cliente/modificar/(?P<pk>\d+)$', ModificarCliente.as_view(success_url="/cliente/")),
     url(r'^cliente/eliminar/(?P<pk>\d+)$', EliminarCliente.as_view(success_url="/cliente/")),
]
