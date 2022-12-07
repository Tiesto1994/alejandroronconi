from django.urls import path
from MVT_Ronconi_app.views import *

urlpatterns = [
    path('',inicio,name="inicio1"),
    path('cultivo',Cultivo,name="cultivo"),
    path('empresas',Empresas,name="empresa"),
    path('compras',Compras,name="compras"),
    path('ventas',Ventas,name="ventas"),
    path('cultivoformulario', cultivoformulario, name="cultivoformulario"),
    path('empresaformulario', empresaformulario, name="empresaformulario"),
    path('comprasformulario', comprasformulario, name="comprasformulario"),
    path('ventasformulario', ventasformulario, name="ventasformulario"),
    path('busquedacultivo', busquedacultivo, name="busquedacultivo"),
    path('buscar', buscar, name="buscar"),
]