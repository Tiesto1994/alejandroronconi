from django import forms

class cultivoform(forms.Form):
    cultivo=forms.CharField(max_length=50)
    gremio=forms.CharField(max_length=50)
    cosecha=forms.CharField(max_length=50)

class empresasform(forms.Form):
    razon_social=forms.CharField(max_length=50)
    cuit=forms.IntegerField()
    gremio=forms.CharField(max_length=50)

class comprasform(forms.Form):
    razon_social=forms.CharField(max_length=50)
    cuit=forms.IntegerField()
    cultivo=forms.CharField(max_length=50)
    volumen=forms.IntegerField()
    cosecha=forms.CharField(max_length=50)
    

class ventasform(forms.Form):
    razon_social=forms.CharField(max_length=50)
    cuit=forms.IntegerField()
    cultivo=forms.CharField(max_length=50)
    volumen=forms.IntegerField()
    cosecha=forms.CharField(max_length=50)
    