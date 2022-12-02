from django.db import models

# Create your models here.

class cultivo (models.Model):
    cultivo=models.CharField(max_length=50)
    gremio=models.CharField(max_length=50)
    cosecha=models.CharField(max_length=50)
    
    def __str__(self):
        return self.cultivo + " " + self.cosecha +" "+ self.gremio

class empresas (models.Model):
    razon_social=models.CharField(max_length=50)
    cuit=models.IntegerField()
    gremio=models.CharField(max_length=50)
    
    def __str__(self):
        return self.razon_social + " " +str(self.cuit) +" "+ self.gremio

class compras (models.Model):
    razon_social=models.CharField(max_length=50)
    cuit=models.IntegerField()
    cultivo=models.CharField(max_length=50)
    volumen=models.IntegerField()
    cosecha=models.CharField(max_length=50)
    
    def __str__(self):
        return self.razon_social + " " + str(self.cuit) +" "+ self.cultivo +""+ str(self.volumen) +""+ self.cosecha 

class ventas (models.Model):
    razon_social=models.CharField(max_length=50)
    cuit=models.IntegerField()
    cultivo=models.CharField(max_length=50)
    volumen=models.IntegerField()
    cosecha=models.CharField(max_length=50)
    
    def __str__(self):
        return self.razon_social + " " + str(self.cuit) +" "+ self.cultivo +""+ str(self.volumen) +""+ self.cosecha 