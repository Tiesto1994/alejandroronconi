from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import Template, loader
from MVT_Ronconi_app.forms import *

# Create your views here.
def Cultivo (request):
    return render(request,"MVT_app/cultivo.html")

def Empresas (request):
    return render(request,"MVT_app/empresa.html")

def Compras (request):
    return render(request,"MVT_app/compra.html")

def Ventas (request):
    return render(request,"MVT_app/venta.html")

def inicio (request):
    return render(request,"MVT_app/inicio.html")

def cultivoformulario (request):

    if request.method=="POST":
        form=cultivoform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            cultivo1=informacion["cultivo"]
            gremio1=informacion["gremio"]
            cosecha1=informacion["cosecha"]
            gran_cultivo=cultivo(cultivo=cultivo1,gremio=gremio1,cosecha=cosecha1)
            gran_cultivo.save()
            return render(request,"MVT_app/inicio.html", {"mensaje":"cultivo creado correctamente"})
    else:
        formulario=cultivoform()


    return render(request,"MVT_app/cultivoformulario.html", {"form":formulario})

def empresaformulario (request):

    if request.method=="POST":
        form=empresasform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            razonsocial5=informacion["razon_social"]
            cuit5=informacion["cuit"]
            gremio5=informacion["gremio"]
            gran_empresa=empresas(razon_social=razonsocial5,cuit=cuit5,gremio=gremio5)
            gran_empresa.save()
            return render(request,"MVT_app/inicio.html", {"mensaje":"empresa creada correctamente"})
    else:
        formulario=empresasform()


    return render(request,"MVT_app/empresaformulario.html", {"form":formulario})

def comprasformulario (request):

    if request.method=="POST":
        form=comprasform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data

            razonsocial1=informacion["razon_social"]
            cuit1=informacion["cuit"]
            cultivo1=informacion["cultivo"]
            volumen1=informacion["volumen"]
            cosecha1=informacion["cosecha"]
            
            gran_compras=compras(razon_social=razonsocial1,cuit=cuit1,cultivo=cultivo1,volumen=volumen1,cosecha=cosecha1)
            gran_compras.save()
            return render(request,"MVT_app/inicio.html", {"mensaje":"compra cargada correctamente"})
    else:
        formulario=comprasform()


    return render(request,"MVT_app/comprasformulario.html", {"form":formulario})

def ventasformulario (request):

    if request.method=="POST":
        form=ventasform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data

            razonsocial2=informacion["razon_social"]
            cuit2=informacion["cuit"]
            cultivo2=informacion["cultivo"]
            volumen2=informacion["volumen"]
            cosecha2=informacion["cosecha"]
            
            gran_ventas=ventas(razon_social=razonsocial2,cuit=cuit2,cultivo=cultivo2,volumen=volumen2,cosecha=cosecha2)
            gran_ventas.save()
            return render(request,"MVT_app/inicio.html",{"mensaje":"venta cargada correctamente"})
    else:
        formulario=ventasform()


    return render(request,"MVT_app/ventasformulario.html", {"form":formulario})

def busquedacultivo (request):
    return render(request,"MVT_app/busquedacultivo.html")

def buscar (request):
    if request.GET["cultivo"]:
        cultivo94=request.GET["cultivo"]
        cultivos=cultivo.objects.filter(cultivo=cultivo94)
        return render(request,"MVT_app/resultadobusqueda.html",{"cultivo":cultivos})
    else:
        return render(request,"MVT_app/resultadobusqueda.html",{"mensaje":"fijate que no esta este cultivo"})